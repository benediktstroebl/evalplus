```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count the number of occurrences of a given substring within the original string, 
    accounting for case-sensitive and overaless matches. 
    Returns a I whole and is case-insensitive and overlapping matches. 
    
    Args:
        string (str): The input string 
        substring (sub): The substring to search for 
    Returns: substring_count: The number of occurrences of substring in string
"""

    # Convert to lowercase for case-insensitive matching
    string = string.lower()
    string = re.sub(sub, "", string)
    string = "".join(string)
    string = re.sub("[^][a-z]", "", string)

    # Initialize counter
    substring_count = 0

    # Use loop and regular expressions to find all occurrences of substring
    for match in re.py.match(string, sub):
        substring_count += 1

    return substring_count
```