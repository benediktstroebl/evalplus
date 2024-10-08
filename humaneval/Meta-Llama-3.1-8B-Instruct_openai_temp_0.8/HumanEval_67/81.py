```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    match = re.search(r'(\d+) apples and (\d+) oranges', s)
    
    if match:
        # Extract the number of apples and oranges from the match
        apples, oranges = int(match.group(1)), int(match.group(2))
        
        # Return the total number of fruits minus the number of apples and oranges
        return n - apples - oranges
    else:
        # If the string does not match the expected pattern, raise a ValueError
        raise ValueError("Invalid input string")

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Expected output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Expected output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Expected output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Expected output: 19
```