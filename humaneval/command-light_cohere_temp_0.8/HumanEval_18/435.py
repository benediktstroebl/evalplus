```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    """
    string = str(string) + str(substring) + str(string[::-1])  # Convert to lowercase and remove duplicates using string.unique reverse() 
    count = 1
    while count < len(string):
        if string[count] == substring:
            count += 1
    return count

# Test the function
test_how_many_times = how_many_times.test_string = "aaaaaaa"
test_substring = "a"
print(test_how_many_times(test_string, test_substring))
```  Output should be 3.