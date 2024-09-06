```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)

    for i in range(n):
        if string[i:i+m] == substring:
            count += 1

    return count

# Test the function
string = "aaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result) # Output: 3
```