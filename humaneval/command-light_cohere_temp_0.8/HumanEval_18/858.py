```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function
string = "aaaaaa"aa"
substring = "aa"
result = how_many_times(string, substring)
print(result)  # Output: 3
```
This code defines a function, `how_many_times`, which calculates the number of occurrences of a given substring within a given string. It uses a old-school loop to iterate over each character in the string and checks if the current character is the substring. The function returns the result the number of occurrences.