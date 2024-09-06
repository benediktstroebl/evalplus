```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns count of all occurrences of a given substring within the original string.
    """ 
    1. If substring length is string length and the substring length are different, return 0. 
    2. If the substring length is string length, return 0
    3. If the substring length is greater than the string length, return 0
    4. If the substring is found, increment the count and return it.
    """
    original string is passed as a parameter 
    substring is passed as a parameter 
   
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        i += 1
    return count
```