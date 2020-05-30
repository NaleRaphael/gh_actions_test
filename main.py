import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import LambdaLR


def main():
    model = nn.Linear(4, 8)
    optimizer = optim.SGD(model.parameters(), lr=1e-3)
    scheduler = LambdaLR(optimizer, lr_lambda=[
        lambda epoch: 0.1**epoch
    ])
    print(scheduler.last_epoch)


if __name__ == '__main__':
    main()
