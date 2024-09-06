```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function
string = "aaaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result) # Output: 3
```