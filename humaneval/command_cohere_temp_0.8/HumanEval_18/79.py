Here's a Python script with a self-contained function that solves the problem you've outlined, including markdown code blocks that demonstrate the behavior of the function and its tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)-len(substring)+1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

# Tests
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('aaaaa', 'aa') == 2
```

This script defines the `how_many_times` function and provides example usage and test cases in the markdown code blocks to verify the function's behavior. Adjust the tests accordingly to cover different scenarios you might encounter.  This function simply iterates through the full string, comparing the substring at different starting positions to the given substring. It counts occurrences regardless of the position and counts overlapping cases too.