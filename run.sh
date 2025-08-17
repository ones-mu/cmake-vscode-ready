#!/bin/bash



# 将shell脚本设置为可执行文件
# chmod +x run.sh
#./run.sh


# 创建 build 目录并运行 CMake
cmake -B build
if [ $? -ne 0 ]; then
    echo "CMake configuration failed. Exiting."
    exit 1
fi

# 输出空行
echo ""

# 构建项目
cmake --build build
if [ $? -ne 0 ]; then
    echo "Build failed. Exiting."
    exit 1
fi

# 输出空行
echo "——————————"

# 运行生成的程序
./output/YourProjectName
if [ $? -ne 0 ]; then
    echo "Execution failed."
    exit 1
fi

