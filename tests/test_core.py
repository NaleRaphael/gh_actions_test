import torch

import mymod
from packaging import version

PYTORCH_VERSION = version.parse(torch.__version__)


def test_lr_scheduler_last_epoch():
    scheduler = mymod.make_scheduler()

    if PYTORCH_VERSION <= version.parse('1.1.0'):
        assert scheduler.last_epoch == -1
    else:
        assert scheduler.last_epoch == 0
