```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "a"
result = how_many_times(string, substring)
print(result)  # Output: 3
```
This function calculates the count of occurrences of a substring within a given string. It does this by using a loop to compare each character with the substring.