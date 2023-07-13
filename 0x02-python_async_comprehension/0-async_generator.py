#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generate random numbers asynchronously.

    Args:
        None

    Yields:
        float: A random number between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)  # Pause execution for 1 second asynchronously.
        yield random.uniform(0, 10)

