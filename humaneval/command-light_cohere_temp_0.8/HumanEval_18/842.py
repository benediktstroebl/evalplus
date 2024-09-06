```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    """
    whole string: str 
    substring: str
    returns: int
    """
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        i += 1
    return count

# Testing the function
string1 = "aaa"
string2 = "aaaa"
string3 = "abc"
string4 = "aaaaaa"

print(how_many_times(string1, string2))  # Output: 3
print(how_many_times(string3, string4))  # Output: 1
print(how_many_times(string2, string3))  # Output: 0
print(how_many_times(string4, string1))  # Output: 2
```