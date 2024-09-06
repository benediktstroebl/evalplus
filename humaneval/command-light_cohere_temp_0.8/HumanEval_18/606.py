```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "a"
print(how_many_times(string, substring))  # Output: 3
```
This code defines a function called `how_many_times` that takes two arguments: a string and a substring. The function uses a loop to count how many times the substring appears in the string, and returns the result.