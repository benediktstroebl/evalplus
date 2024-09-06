Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in the given string, ignoring case.
    Args: 
        string: str - The input string
    
    Returns: 
        int - Number of distinct characters
    """
    return len([c for c in string.distinct() if c.isdigit() and distinct(c)])
```
The script defines a function `count_distinct_characters` that takes a string as an argument and returns an integer representing the count of distinct characters. 

The function uses a list comprehension to filter out all characters from the input string that are also present in the string at least, which effectively means they are distinct characters. 
The function then uses the `len` function to count the number of elements in the resulting list, which corresponds to the number of distinct characters in the input string.