```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of string
    Returns:
        string
    """
    return ''.join(strings)

# Test case 1
test_case1 = [
    "Hello, ", "World! "


def test_function1():
    return concatenate(test_case1)

# Test case 2
test_case2 = ["a", "bc"]

def test_function2():
    return concatenate(test_case2)

# Test case 3
test_case3 = ["abc", "d"]

def test_function3():
    return concatenate(test_case3)

print(test_function1()) # Output: Hello, World!World!
print(test_function2()) # Output: abc
print(test_function3()) # Output: abcd
```