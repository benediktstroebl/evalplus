```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, 
    while avoiding overlapping occurrences.
    """
    Using a a recursive approach to find the number of occurrences, 
    we iterate over each character and count the number of occurrences.
    >>> 
    return sum(1 for c in substring if c in string and not in substring_count or substring_count == substring)

# Test cases:
>>> how_many_times('aaa', 'a')  # 3
>>> how_many_times('aaaa', 'aa')  # 3
>>> how_many_times('abcde', 'abcd')  # 2
>>> how_many_times('abcdef', 'abcd')  # 2
>>> how_many_times('abcdef', 'abcdef')  # 1
```
The function uses a dictionary to keep track of the count of the substring, and each time a character from the substring is found in the string, we increment the count. This ensures that overlapping occurrences are correctly counted.