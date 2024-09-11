```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges
    match = re.search(r'(\d+) apples and (\d+) oranges', s)
    
    if match:
        apples = int(match.group(1))
        oranges = int(match.group(2))
        
        # Return the number of mango fruits by subtracting apples and oranges from the total
        return n - apples - oranges
    else:
        # If the input string does not match the expected pattern, return -1
        return -1

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string `s`, and then returns the number of mango fruits by subtracting these numbers from the total `n`. If the input string does not match the expected pattern, it returns -1.