```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits given the string representation of apples and oranges
    and the total number of fruits in the basket.

    Args:
    s (str): A string representing the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    match = re.search(r'(\d+) apples and (\d+) oranges', s)
    
    # If a match is found, extract the numbers
    if match:
        apples, oranges = map(int, match.groups())
        
        # Return the difference between the total number of fruits and the sum of apples and oranges
        return n - apples - oranges
    else:
        # If no match is found, return an error message
        return "Invalid input format"

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string. It then calculates the difference between the total number of fruits and the sum of apples and oranges to find the number of mango fruits.