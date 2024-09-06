Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings.index(max(strings, key=len))
        return strings[max_idx]
```
This script includes the `longest` function that takes a list of strings as input and returns the longest string according to the problem statement. It also includes an example usage and a test case to ensure the function behaves as expected. 

Here's an example usage scenario:
```python
print(longest(['a', 'bb', 'ccc']))  # Outputs: ccc
```
And here is the self-contained test case:
```python
def test_longest():
    # Test case 1: Empty list
    assert longest([]) is None

    # Test case 2: Single string
    assert longest(['a']) == 'a'

    # Test case 3: Multiple strings of different lengths
    assert longest(['a', 'bb', 'ccc']) == 'ccc'

    # Test case 4: Multiple strings of the same length
    assert longest(['aa', 'bb', 'cc']) == 'aa'

    # Test case 5: Mixed strings
    assert longest(['a', 'bb', 'ccc', 'aaa']) == 'ccc'

test_longest()
```

Note that the `test_longest` function tests the `longest` function with the five different cases mentioned in the prompt.