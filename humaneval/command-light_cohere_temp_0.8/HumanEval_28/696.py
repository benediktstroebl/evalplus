```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join("".join(string for string in strings))

# additional test cases for documentation
test_concat = []
test_concat.add("").join(["a", "bc", "c"])
test_concat.add([["hello", "world"])
test_concat.add([""))
print("Test results:", concatenate(test_concat))
```