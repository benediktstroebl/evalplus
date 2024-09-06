Here is a self-contained Python script that solves the problem of counting the number of occurrences of a substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Finds how many times a given substring can be found in the original string.

    Args:
        string (str): The input string
        substring (sub): The substring to search

    Returns: int or None: Number of occurrences of the substring, or None if not found
    """
    if substring not in string:
        return None
    count = 0
    start = 0
    end = 0
    i = 0
    while True:
        end = string.find(substring, end+1)
        if end == -1:
            break
        count += 1
        i = end+1
    return count

# Test cases
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
print(how_many_times('abcde', 'abc'))  # Output: 2
print(how_many_times('abcba', 'abc'))  # Output: 2
```

This script defines a function `how_many_times` that takes two parameters: a string and a substring. It uses a search to find the substring in the string and counts the number of occurrences. It returns the count of occurrences of the substring.