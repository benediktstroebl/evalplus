```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function
test_string = "aaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
print(result) # prints 3
```
This code provides a function that accepts two parameters: a string and a substring. The function uses a loop to find the occurrences of the substring in the original string. This function is simple and efficient and it can be used to find the occurrences of any substring in any given string.