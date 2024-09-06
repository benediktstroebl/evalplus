```python
def count_distinct_characters(string: str):
    """
    Returns the number of distinct characters in the string regardless of case.
    Args: 
        string (str): A string

    Returns: 
        int: Number of distinct characters
    """
    string = string.split()
    string = [char for char in string if char not in string]
    return len(string)

# Test the function
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4    
```  This code defines a function `count_distinct_characters` which takes a string as input and returns the count of distinct characters in that string, regardless of their case. It uses the `split` method to convert the string into a list of characters, then it iterates through the characters in the string and adds them to a new list if the character is not in the original string.