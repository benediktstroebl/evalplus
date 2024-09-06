```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string
    Returns: str - The concatenated string
    """
    return ''.join(''.join(strings)  # type hint: str(xs) gives xs which is a string, hence no type hint here)

# Test case with empty list
test_concatenate_empty()
def test_concatenate_empty():
    assert concatenate([]) == ''

# Test case with one string
test_concatenate_single()
def test_concatenate_single():
    assert concatenate(['a']) == 'a'

# Test case with two strings
test_concatenate_two()
def test_concatenate_two():
    assert concatenate(['a', 'b']) == 'ab'

# Test case with list of strings
test_concatenate_list()
def test_concatenate_list():
    assert concatenate([['a'], ['b', 'c'], ['d']]) == 'ad'

if __name__ == "__main__":
    unittest.py()

```

The provided Python script defines a `concatenate` function that takes a list of strings and concatenates them into a single string. It also comes with test cases to ensure the correctness of the `concatenate` function.