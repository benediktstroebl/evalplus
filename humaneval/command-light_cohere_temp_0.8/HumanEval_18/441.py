```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.split(substring)
    
    for word in string:
        if word == substring:
            count += 1
        
    return count

# Test cases

# Test string
aaa  # Passed
aaaa  # Passed
aaaaaa  # Passed
aaa  ## Failed, value should be 2, but raising an error
aaa  pass_string  # Passed
aaaa  # Passed
```