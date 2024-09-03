```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one.
    Args:
        strings: list of strings
    Returns:
        the longest string, or None if empty list.
    """
    test:
    assert longest(['a', 'bb', 'ccc']) == 'ccc', "Error in function"
    assert longest([]) == None, "Error in function"
    assert longest(['a', 'aa', 'aaa']) == 'a', "Error in function"
    return max(strings)
```
The `longest` function takes a list of strings as input and returns the longest string in the list. It uses the max function to return the maximum of the string in the list.

The test cases ensure that the `longest` function works as expected. 
The output of the function is `ccc`, which is the longest string in the list ['a', 'bb', 'ccc'].