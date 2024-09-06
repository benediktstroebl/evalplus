```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = str(string)  # convert to lowercase for case-insensitive search
    sub = str(substring)
    
    for char in sub:
        count += string.find(char) != None
    return count

# test case
print(how_many_times('aaaa', 'aa'))
```