```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring within the original string.
    while iterating substring over the result is the total occurrences.
    """
    basic implementation with the following steps:
    - Initialize a variable count to 0
    - Use a while loop to iterate through each character in the substring
    - Increment the count with every character match
    - Return the final count.
    """ 
    tested cases:
    >>> how_many_times('aaa', 'aa')
    3
    >>> how_many_times('aaaa', 'aa')
    4
    >>> how_many_times('abcde', 'abc')
    3
    >>> how_many_times('abcda', 'abc')
    3
    """

    return len(string.find(substring))
```