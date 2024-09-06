Here is a Python script that contains a self-contained function that solves the problem:
```python
def how_many_times(string, substring): 
    """ Count the frequency of a substring in a given string.
    # Test if substring exists in the string 
    if substring in string:
        return 1
    # Initialize a count of 0 for substring
    count = 0
    # Loop through the string
    for i in string:
        if i == substring:
            count += 1
    return count

# Test the function
test_string = "aaaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
print(f"There are {result} occurrences of '{test_substring}' in the string.")
```

This script provides a function that accepts two parameters: a string and a substring. It then checks if the strings are equal, and counts the number of times the substring appears in the string. The function returns the result.