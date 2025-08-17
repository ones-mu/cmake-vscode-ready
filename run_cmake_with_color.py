import os
import subprocess
import multiprocessing
import sys
from colorama import init, Fore, Back, Style

# 初始化colorama（自动处理Windows上的颜色支持）
init(autoreset=True)

def print_header(message):
    print(f"{Fore.CYAN}{Style.BRIGHT}==> {message}{Style.RESET_ALL}")

def print_success(message):
    print(f"{Fore.GREEN}{Style.BRIGHT}✓ {message}{Style.RESET_ALL}")

def print_warning(message):
    print(f"{Fore.YELLOW}{Style.BRIGHT}⚠ {message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}{Style.BRIGHT}✗ {message}{Style.RESET_ALL}", file=sys.stderr)

def run_command(cmd, cwd=None):
    """运行命令并返回是否成功"""
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Command failed: {' '.join(cmd)}")
        print_error(f"Error: {e}")
        return False
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        return False

def run_cmake_commands():
    # 获取CPU核心数
    nproc = multiprocessing.cpu_count()
    
    # 创建build目录（如果不存在）
    build_dir = "build"
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    
    # 1. 运行 cmake -B build
    print_header("Configuring project with CMake")
    configure_cmd = ["cmake", "-B", build_dir]
    if not run_command(configure_cmd):
        sys.exit(1)
    
    # 2. 运行 cmake --build build -j${nproc}
    print_header(f"Building project with {nproc} jobs")
    build_cmd = ["cmake", "--build", build_dir, "-j", str(nproc)]
    if not run_command(build_cmd):
        sys.exit(1)
    
    # 3. 运行 ./build/bin/YourProjectName
    print_header("Running the executable")
    executable_path = os.path.join(build_dir, "bin", "YourProjectName")
    if not os.path.exists(executable_path):
        print_error(f"Executable not found at {executable_path}")
        sys.exit(1)
    
    run_cmd = [executable_path]
    if run_command(run_cmd):
        print_success("Build and run completed successfully!")
    else:
        sys.exit(1)

if __name__ == "__main__":
    run_cmake_commands()