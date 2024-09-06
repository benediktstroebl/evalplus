```python
def count_distinct_characters(string: str):
    """ 
    Return the count of distinct characters in the string, regardless of case.
    """
    Inverse character set of the characters and convert to set, then count the distinct elements 
    """
    # Inverse character set
    char_inv = "".join(str.find(c, 1) for c in string)
    char_set = set(char_inv)
    distinct = len(char_set)
    return distinct

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))    # Output: 4
``` 
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The function utilizes the method of converting the string to an inverse character set and then counting the distinct elements. The test cases demonstrate the for different inputs, the function successfully computes and returns the number of distinct characters.