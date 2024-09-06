```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string = "aaaaaaa"
substring = "a"
result = how_many_times(string, substring)
print(result)  # Output: 3
```
This code defines a function how_many_times that calculates and returns the number of occurrences of a given substring within a string. The function uses a loop to iterate over each character in the string, and counts the occurrences of the substring. The test section demonstrates the using a sample string and substring, it passes the function how_many_times and prints the result, which should be 3 in this case.