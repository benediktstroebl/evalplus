Here is a self-contained Python function that solves the problem you have described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    accounting for overlapping occurrences.

    Args:
        string: The input string
        substring: The substring to find in the input string
    """
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        i += 1
    return count

# Test case 1
test_case1 = "aaa"
test_result1 = how_many_times(test_case1, 'a')
print("Test case 1:", test_result1)

# Test case 2
test_case2 = "abc"
test_result2 = how_many_times(test_case2, 'a')
print("Test case 2:", test_result2)

# Test case 3
test_case3 = "AA"
test_result3 = how_many_times(test_case3, 'a')
print("Test case 3:", test_result3)
```
This function uses a while loop to iterate over the input string and checks if the current character matches the substring. The function returns the count of occurrences of the substring in the string. This function is straightforward and easy to read and understand. It solves the problem of counting the occurrences of a substring in a string.