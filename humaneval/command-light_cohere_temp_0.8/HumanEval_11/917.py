```python
import stringio
from typing import List
def string_xor(a: str, b: str) -> str:
    """ XOR two strings containing only digits using type hints
    """ return stringio.make(repr(f"{0{a}{b}{a}{b}}"), encoding="utf-8").decode()
# Example usage
test_cases = [
    ("010", "110"),
    ("1010", "001"),
    ("000111", "11001"),
    ("121314", "2131"),
]
for a, b in test_cases:
    print(f"Result: {string_xor(a, b)})
```