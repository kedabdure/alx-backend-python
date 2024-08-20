#!/usr/bin/env python3
"""
0-async_generator
"""
import asyncio
import random


async def async_generator():
    """generate random number

    Yields:
        int: random int between 0 - 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
