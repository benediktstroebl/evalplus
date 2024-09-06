import unittest
from unittest.mock import Mock, call
def sort_numbers(numbers: str) -> str:
    return ' '.join(sorted(numbers.split()))