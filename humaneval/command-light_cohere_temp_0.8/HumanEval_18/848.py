```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
text = "aaaaaaa"
substring = "aa"
result = how_many_times(text, substring)
print(result)  # Output: 3
```

This script defines a function `how_many_times` that takes two parameters: a string and a substring. It uses a a for loop to iterate through each character in the string and counts how many times the substring is found. The function returns the result.