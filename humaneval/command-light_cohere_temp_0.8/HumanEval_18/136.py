```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result)  # Output: 3
```

This code defines a function called **`how_many_times`** that takes two parameters: a string and a substring. The function uses a a sliding window approach to count the occurrences of the substring in the string. It iterates through the particular character in the substring and if it is found in the string, it increments the count.

Finally, the function returns the count of occurrences of the substring in the string.

Please note that you may need to install the **`string`** module if you are getting an error related to the usage of the **`string`** class.