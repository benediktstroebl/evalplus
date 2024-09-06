```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.find(substring, 0, len(string))
    while string != None:
        count += 1
        string = string.find(substring, 0, len(string))
    return count

# Test the function
string = "aaaaaaa"
substring = "aa"
print(how_many_times(string, substring))
```