```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    accounting for cases where the substring is longer than the original string.
    """
   
    definition of a more general string match function
    """
    count = 0
    l = len(substring)
    i = 0
    while i < l:
        if substring[i] in string:
            count += 1
        i += 1
    return count

# Test the function
string = "aaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result)
```