```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string = "aaaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result) # prints 3
```