cmake_minimum_required(VERSION 3.21)

project(YourProjectName
    VERSION 1.1
    LANGUAGES CXX
    DESCRIPTION " your project description here"
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)


file(GLOB_RECURSE cpp_sources "src/*.cpp")


include_directories("include")

add_executable(${PROJECT_NAME} ${cpp_sources})