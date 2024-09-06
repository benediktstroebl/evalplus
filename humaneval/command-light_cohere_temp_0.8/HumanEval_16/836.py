```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a given string, regardless of case.
    return: 
    """ Counts the string length and returns the count of distinct characters."""
    
    string = string.lower()  #\need special case to consider
    return len(set(string))

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('jerry') == 4
``` 
This Python code defines a function called `count_distinct_characters` that calculates the count of distinct characters in a given string. The function utilizes the string.s and converts it to lowercase to ensure case-insensitive counting. The function returns the unique character count. The test cases validate the the correctness of the function's behavior.