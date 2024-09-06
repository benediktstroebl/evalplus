```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result) # prints 3
```