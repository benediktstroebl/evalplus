Here's the function that finds how many times a given substring can be found in the original string, while also accounting for case and spaces:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring appears in the original string, 
    accounting for case and spaces.
    """
    using regular expressions and 
    O(n) where n is string length, and O(m) where m is substring length
    """
    # Ensure that substring is all lowercase and contains only alphanumeric
    # characters and spaces
    substring = substring.replace('a-z')

    string = ' '.join(string)
    count = 0
    for char in substring:
        if char in string:
            count += 1

    return count

# Test cases
print(how_many_times('aaa', 'aa')) # Should return 3
print(how_many_times('abcde', 'abc')) # Should return 5
print(how_many_times('aaaaaa', 'aa')) # Should return 6
```