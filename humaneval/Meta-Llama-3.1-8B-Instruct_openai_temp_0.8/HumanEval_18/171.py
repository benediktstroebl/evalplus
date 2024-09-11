```markdown
### Substring Frequency Counter
#### A Python function to count the occurrences of a substring in a string

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the string.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0  # Initialize a counter variable
    for i in range(len(string) - len(substring) + 1):  # Iterate over the string
        if string[i:i+len(substring)] == substring:  # Check if the substring matches
            count += 1  # Increment the counter if it does
    return count  # Return the total count
```

You can use this function like this:
```python
print(how_many_times('abcdef', 'abc'))  # Output: 1
print(how_many_times('abcdef', 'cde'))  # Output: 1
print(how_many_times('abcdef', 'd'))  # Output: 1
```

Note that this function has a time complexity of O(n*m), where n is the length of the string and m is the length of the substring. This is because we're using a linear search approach to find the substring within the string. If you need a more efficient solution, you may want to consider using a KMP (Knuth-Morris-Pratt) algorithm or a regex approach.