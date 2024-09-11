```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits 
    and a string describing the number of apples and oranges.

    Parameters:
    s (str): A string representing the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    
    # If the string matches the expected pattern, extract the numbers
    if match:
        num_apples = int(match.group(1))
        num_oranges = int(match.group(2))
        
        # Return the total number of fruits minus the number of apples and oranges
        return n - num_apples - num_oranges
    
    # If the string does not match the expected pattern, return None
    else:
        return None

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as inputs. It uses regular expression to extract the numbers of apples and oranges from the string, and then returns the total number of fruits minus the number of apples and oranges. The function includes docstrings to describe its purpose and parameters. The script also includes test cases to demonstrate the function's behavior.