```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = str. FindSubstr(string, substring)
    while True:
        index = next(string.find(substring))
        if index == None:
            break
        count += 1
    return count

#Test cases
string = "aaaaaa"
substring = "aa"

result = how_many_times(string, substring)
print(result)  # Output: 3
```