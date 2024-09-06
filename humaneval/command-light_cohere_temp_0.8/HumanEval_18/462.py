```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    counting overlapping matches.

    Args: 
    - string: The input string 
    - substring: The substring to find in the string 

    Returns: 
    - int: Number of times the substring occurs in the string
    """
    return sum(1 for x in string.groupify(substring in string))

# Testing the function
test_string = "aaaaaaa"
test_substring = "a"
test_result = how_many_times(test_string, test_substring)
print("Test string:", test_string) 
print("Test substring:", test_substring) 
print("Number of times:", test_result)
```