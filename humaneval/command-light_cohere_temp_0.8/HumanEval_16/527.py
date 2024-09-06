```python
def count_distinct_characters(string: str):
    """ 
    Given a string, finds out how many distinct characters (case insensitive) it consists of and returns that count 

    Parameters:
    string (str): String input to process

    Returns:
    count: Number of distinct characters 
    """
    return len({c for c in string if c.isalpha()} )  # the detailed explanation please refer to the code snippet above.