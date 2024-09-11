```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    i = 0
    while i < len(string):
        if string[i:i+len(substring)] == substring:
            count += 1
            i += 1  # Only increment i once, so we don't count the same substring twice
        i += 1
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 2
```

However, a more Pythonic and efficient way to solve this problem would be to use the `count` method of the string class, which counts the number of non-overlapping occurrences of the substring. 

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    return len(string) // len(substring)

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 2
```

This version of the function will not work correctly, because it does not account for overlapping occurrences. Here is a revised version:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    return sum(s.startswith(substring) for s in [string[i:] for i in range(len(string))])

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 2
```
This version of the function generates all substrings of the original string (from the beginning to the end of the string) and checks whether each of them starts with the given substring. It counts these occurrences and returns the sum.