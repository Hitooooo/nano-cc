#!/usr/bin/env python3

import os
import subprocess

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

if os.getenv("ANTHROPIC_BASE_URL"):
    os.environ.pop("ANTHROPIC_AUTH_TOKEN", None)


client = Anthropic()

def main():
    print("Hello from nano-cc!")


if __name__ == "__main__":
    main()
