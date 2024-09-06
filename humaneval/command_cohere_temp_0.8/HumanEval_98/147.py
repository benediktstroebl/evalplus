Here's the Python script, including a self-contained function `count_upper()` that solves the problem as described in the code block:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices of the string. It then returns the count. The function utilizes Python's built-in `isupper()` method to determine if a character is uppercase and iterates through the string in increments of 2 to identify vowels in even indices.

The problem is framed such that the input string can be any combination of characters, so the provided solution is optimized to only consider uppercase vowels in even indices, as specified by the problem statement. This solution efficiently solves for the given condition without unnecessarily parsing the entire input string.