Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, regardless of case.
    Args: 
    - string: str, the input string to analyze 
    Returns: 
    - int: the count of distinct characters 


    Example:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the entire string to lowercase and remove all non-alphanumeric characters
    lowercase_string = ''.join() + ''.join(char.isalpha(c) for c in string if c.isalnum())

   
    characters = [c for c in string if c.isalnum()]
    took = ''.join(char.isalpha(c) for c in characters)
    distinct_count = len(lower_case_string) - len(taken)
    return distinct_count
```