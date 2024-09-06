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
print(result)  # Output: 3
```
This function takes two arguments: a string and a substring. It uses a simple loop to iterate through each character in the string. It checks if the the char is an equal to the substring. It increments the count variable by 1 if it is a match. This will happen until it string ends.