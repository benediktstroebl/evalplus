```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given a string 
    representing the number of apples and oranges and an integer representing the total 
    number of fruits in the basket.

    Parameters:
    s (str): A string that represents the total number of the oranges and apples 
             and a description of the basket in the format "x apples and y oranges".
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """

    # Use regular expression to extract the number of apples and oranges from the string
    match = re.search(r'(\d+)\D+(\d+)\D+oranges', s)
    
    # If the string matches the expected format
    if match:
        # Extract the number of apples and oranges from the match
        apples, oranges = map(int, match.groups())
        
        # Return the total number of fruits minus the number of apples and oranges
        return n - apples - oranges
    
    # If the string does not match the expected format, raise a ValueError
    else:
        raise ValueError("Invalid input format")

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # -> 19
```
This script uses the `re` module to extract the number of apples and oranges from the input string using a regular expression. It then returns the total number of fruits minus the number of apples and oranges. If the input string does not match the expected format, it raises a `ValueError`.