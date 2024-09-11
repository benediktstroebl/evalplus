```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expressions to extract the number of apples and oranges from the string
    apples_oranges = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    apples = int(apples_oranges[0])
    oranges = int(apples_oranges[1])
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    return n - apples - oranges

# Test the function with example inputs
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the number of apples and oranges from the input string, and then calculates the number of mango fruits by subtracting these numbers from the total number of fruits. The result is returned as an integer.