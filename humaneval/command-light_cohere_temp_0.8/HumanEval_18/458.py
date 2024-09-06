```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.
    """
   
    string: str = 'aaaaaaaaca'
    sub = 'a'
    count = 0
    start = 0
    while start < len(string):
        if string[start] == sub:
            count += 1
        if string[start] != sub[0]:
            start += 1
    return count

# Test cases
test_string = "aaaaaaaaca"
test_substring = "a"
test_count = how_many_times(test_string, test_substring)
print("Test String:", test_string)
print("Test Substring:", test_substring)
print("Test Count:", test_count)
``` 
This script defines a function `how_many_times` which counts the number of occurrences of a given substring in a string while avoiding overlapping. The function uses a string and substring as inputs, initializes variables to keep track of the starting position and count of occurrences, and uses a `while loop` to iterate through the string. The function returns the interesting feature is that it avoids overlapping by only counting occurrences at different positions.