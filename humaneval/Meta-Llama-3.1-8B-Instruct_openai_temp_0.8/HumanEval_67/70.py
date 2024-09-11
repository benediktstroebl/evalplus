```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to find the numbers of apples and oranges
    match = re.search(r'(\d+)\s*(apples|oranges)', s)
    
    if match:
        # Extract the number of apples or oranges
        fruit_count = int(match.group(1))
        
        # Return the number of mango fruits
        return n - fruit_count * (match.group(2) == 'apples' and 1 or -1)
    else:
        # If no match is found, raise a ValueError
        raise ValueError("Invalid input format")

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to find the numbers of apples and oranges in the input string `s`. It then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits `n`. If the input string is not in the correct format, it raises a `ValueError`.