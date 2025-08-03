"""The nes-py NES emulator for Python 3."""
from .nes_env import NESEnv


__version__ = "8.2.1"

# explicitly define the outward facing API of this package
__all__ = [NESEnv.__name__]
