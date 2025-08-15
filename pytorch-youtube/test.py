import torch

# PyTorchのバージョン確認
print("Torch version:", torch.__version__)

# CUDA（GPU）サポートの有無確認
print("CUDA available:", torch.cuda.is_available())

# 実際にテンソルを作ってみる
x = torch.rand(3, 3)
print("Random tensor on CPU:\n", x)
