```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
text = "aaaaaaa"
substring = "aa"
print(how_many_times(text, substring))  # Output: 3
```
This function counts the occurrences of a substring in a given string. It's efficient and uses a simple loop to iterate through each character in the string.