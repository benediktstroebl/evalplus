```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Parameters:
    s (str): A string that represents the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    
    # If a match is found, extract the numbers
    if match:
        apples, oranges = int(match.group(1)), int(match.group(2))
        
        # Return the total number of fruits minus the numbers of apples and oranges
        return n - apples - oranges
    else:
        # If no match is found, raise an exception
        raise ValueError("Invalid input string")
```

### Example Usage:

```python
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string. If the string matches the expected format, it calculates and returns the total number of fruits minus the numbers of apples and oranges. If the string does not match the expected format, it raises a ValueError.