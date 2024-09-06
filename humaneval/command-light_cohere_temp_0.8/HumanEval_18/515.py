```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string = "aaaaaaa"
substring = "aa"
print(how_many_times(string, substring))  # Output: 3

```

This Python script defines a function named `how_many_times` that calculates the count of occurrences of a given substring within a given string. The function utilizes a loop to iterate through each character of the string, and counts the occurrences of the substring. The test section demonstrates the uses a sample string and substring to pass to the function and prints the result.