Here's a Python function that solves the problem of finding the number of times a substring occurs in a given string. The function also accounts for overlapping instances of the substring:
```python
def how_many_times(string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    
    counter = 0
    length = len(substring)
    
    for i in range(len(string) - length + 1):
        if string[i:i+length] == substring:
            counter += 1
    
    return counter
```

To use this function, you can call it with a string and a substring, as demonstrated in the docstring:
```python
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
>>> how_many_times('abacabad', 'aba')
2
```

The function also handles edge cases where either the main string or the substring is empty, setting the count to 0 in such cases.