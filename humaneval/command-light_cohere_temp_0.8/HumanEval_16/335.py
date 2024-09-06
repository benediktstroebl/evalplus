```python
def count_distinct_characters(string: str) -> int:
    """
        Count the distinct characters in a given string regardless of the case.
        Args: 
            string (str): str -- The input string
        Returns: 
            int -- The number of distinct characters 
    """
    return len([c for c in string.isupper()])
``` 
This code defines a function 'count_distinct_characters' which accepts a string as an argument and returns the number of distinct characters in that string, regardless of their case.  The function uses the simple list comprehension to identify distinct characters and counts them.