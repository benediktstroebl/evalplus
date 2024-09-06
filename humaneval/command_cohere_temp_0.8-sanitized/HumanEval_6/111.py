import unittest
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [max(nesting, 1 if char in '(){}' else 0)
            for char, nesting in enumerate(zip(*[iter(s)] * 2), 1)]