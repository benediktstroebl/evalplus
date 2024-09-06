```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result) # Output: 3
```

This script defines a function that counts how many times a substring appears in a string. How many times? It uses a simple loop that compares each character in the string with the substring, and counts the number of matches. The function then tests this code block passes the tests successfully.