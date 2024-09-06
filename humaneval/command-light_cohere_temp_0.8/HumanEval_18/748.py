```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find the number of occurrences of a substring in a string.
    string = string.split()
    rely on list comprehension and simple loops.
    counter = 0
    substring = substring.split()
    rely on list comprehension and simple loops
    for i, char in substring: 
        if char in string:
            counter += 1
        string = string.split(substring) 
    return counter
```