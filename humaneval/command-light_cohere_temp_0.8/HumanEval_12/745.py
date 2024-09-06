```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the length of the longest string in the list.
    Args:
    strings (List[str]): List of strings.
    Returns: first one in case of multiple strings of the same length.
    Returns None if the
    input list is empty.
    """
    Python  syntax
    `None` is a special value that represents the absence of a value. This function is designed to handle the case of an empty input list by returning `None`. 

def test_longest():
    """
    Test cases for longest function
    """
    assert longest([]) is None, "The function should return None for an empty list"
    assert longest(['a']) == 1, "The function should return the length of 'a' for a single string"
    assert longest(['a', 'bb', 'ccc']) == 3, "The function should return the length of 'ccc' for a list with three strings"
    assert longest(['aa', 'bb', 'ccc']) is None, "The function should return None for lists with repeated strings"
    assert longest(['aa']) == 1, "The function should return the length of 'aa' for a single string"

if __name__ == "__main__":
    test_longest()
```
This script provides a Python function called longest, which takes a list of strings as input and returns the length of the longest string in the list. The function uses an `None` return type to handle empty lists. The test_longest function contains a series of test cases that verify the correctness of the longest function with different input scenarios.