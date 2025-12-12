import torch

model = torch.hub.load("facebookresearch/pytorchvideo:main", "x3d_m", pretrained=True)
print(model._meta["classes"])

