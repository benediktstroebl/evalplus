```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
text = "aaaaaa"
substring = "aa"
result = how_many_times(text, substring)
print(result)
```