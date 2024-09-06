Here is a Python script that defines a function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, ignoring case.
    Args:
        string (str): str -- input string
    Returns:
        int -- number of distinct characters
    """
    return len({c.isupper() for c in string})

# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('jerry'), 4)
assertEqual(count_distinct_characters(' '''), 0)
assertEqual(count_distinct_characters('\t'), 1) # \t is also a distinct character

``` 
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, without considering case sensitivity. 

The function uses a dictionary comprehension to count the unique characters in the string, and then returns the length of this dictionary. 
The test cases demonstrate the function's behavior for various inputs.