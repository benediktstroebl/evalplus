Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings.index(max(strings))
        return strings[max_idx]
```
This script includes the `longest` function that takes a list of strings as input and returns the longest string according to the problem statement. It also includes an example usage and a test case to ensure the function behaves as expected. 

Here's an example usage of the function:
```python
print(longest(['a', 'bb', 'ccc']))  # Outputs: ccc
```
And here is the test case:
```python
def test_longest():
    # Empty list
    assert longest([]) is None

    # List with one string
    assert longest(['a']) == 'a'

    # List with multiple strings
    assert longest(['a', 'bb', 'ccc']) == 'ccc'

    # List with multiple equal longest strings
    assert longest(['a', 'b', 'b', 'c']) == 'b'

    # List with one string that is the longest
    assert longest(['a', 'b', 'c', 'a']) == 'a'
```