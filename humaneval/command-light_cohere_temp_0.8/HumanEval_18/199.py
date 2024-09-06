```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    string += ' ' + substring 
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        string[i] = string[i+1]
        i += 1
    return count
# Example usage
text = "aaa"
substring = "aa"
print(how_many_times(text, substring))  # Output: 3
```