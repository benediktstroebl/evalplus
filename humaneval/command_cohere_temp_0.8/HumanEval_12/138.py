Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
```python
# The module name can be omitted when submitting a single function
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(set([len(s) for s in strings])) == 1 else longest_str[0]

# Test cases
def test_longest():
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['aaa', 'aa', 'ab']) == 'aaa'
    assert longest(['aaaa', 'aa', 'aabb']) == 'aaaa'

# Run the tests when the script is directly executed
if __name__ == "__main__":
    test_longest()
```

The function `longest` takes a list of strings as input and returns the longest string. It handles cases where there are multiple longest strings and when the list is empty.

The test cases are placed after the function definition. They check various scenarios to verify the correctness of the `longest` function.

When the script is directly executed, the test cases are run automatically, and the output will indicate whether the tests pass or fail. 

To execute the code snippet above separately, remove the `if __name__ == "__main__":` block, and save the code in a Python file (e.g., `longest.py`). Then, you can run the file using the Python interpreter: `python longest.py`