```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.split(substring)
    
    for word in string:
        if word == substring:
            count += 1
    
    return count

# Test the function
test_how_many_times = {
    "aaa"
    "aa"
    "aaaa"
    "aaaaaa"
    pass
}

print(f'The number of times the substring "a" appears is: {test_how_many_times["aaa"]}')
```