```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    """
    unique_substring_count = set()  # Using set to store unique substrings
    for char in substring:
        unique_substring_count.add(char)
    string = string.replace(char, unique_substring_count)
    return len(string)

# Test cases
print(how_many_times('aaa', 'aa'))  # Output: 3
print(how_many_times('abcde', 'ab'))  # Output: 3
print(how_many_times('hello world', 'world'))  # Output: 5
print(how_many_times('aa', 'a'))  # Output: 0
```