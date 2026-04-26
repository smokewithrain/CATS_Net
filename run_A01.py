import sys
import runpy  # 1. 导入 runpy 模块

# 2. 在这里设置参数，模拟命令行输入
sys.argv = [
    "A01_ImageNet.main",
    "-ne", "5",
    "-bs", "512",
    "-lr", "0.001",
    "-nc", "1000",
    "-ss", "20",
    "--dataset", "cifar100",
    "--model_name", "resnet50",
    "--fix_fe",
    "--use_pretrain",
    "--use_orthg"
]

# 3. 以脚本方式运行模块
# 这行代码的效果完全等同于在命令行执行: python -m A01_ImageNet.main ...
runpy.run_module('A01_ImageNet.main', run_name='__main__', alter_sys=True)