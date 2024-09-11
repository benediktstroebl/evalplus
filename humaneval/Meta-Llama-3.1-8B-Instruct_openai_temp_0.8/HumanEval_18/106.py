```markdown
### Problem: Counting Substring Occurrences

The following Python script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the original string, including overlapping cases.

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found in the original string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    for i in range(len(string)):
        # Check if the substring matches the string at the current index
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
```

### Example Use Cases

```python
# Test the function with the given examples
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3

# Additional test cases
print(how_many_times('abcabcabc', 'abc'))  # Output: 3
print(how_many_times('abcdef', 'def'))  # Output: 1
print(how_many_times('abcdef', 'ghi'))  # Output: 0
```

### Explanation

The function `how_many_times` uses a simple loop to iterate over the original string. At each index `i`, it checks if the substring matches the string at the current index by comparing the substring with the string from index `i` to `i+len(substring)`. If the substring matches, the count is incremented by 1. The function returns the total count after iterating over the entire string.