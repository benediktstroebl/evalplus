Here is a Python script that defines a function `count_distinct_characters`, which calculates the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, ignoring case.
    Args: 
        string (str): The input string

    Returns: 
        int: Number of distinct characters
    """
    string = string.lower()  # transform_string(string) 
    return len(set(string))

# Test case 1
test_case1 = "xyzXYZ"
assert count_distinct_characters(test_case1) == 3

# Testcase 2
test_case2 = "jerry"
assert count_distinct_characters(test_case2) == 4
```
This script provides a straightforward function that transforms all characters to lowercase and then counts the distinct characters. 

The test cases are also provided to verify the function's behavior.