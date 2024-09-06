Here's a self-contained Python script with a function that finds the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count
# Test the function
test_string = "aaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
print("Result:", result)
``` 
This function iterates over each character in the string and checks if the substring is found at that position. It then counts the _ the number of positions where the substring was found.