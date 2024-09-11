```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits,
    and a string describing the number of apples and oranges.

    Parameters:
    s (str): A string representing the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges
    match = re.search(r'(\d+) apples and (\d+) oranges', s)
    
    # If the pattern is found, extract the numbers
    if match:
        num_apples = int(match.group(1))
        num_oranges = int(match.group(2))
        # Return the total number of fruits minus the number of apples and oranges
        return n - num_apples - num_oranges
    else:
        # If the pattern is not found, return an error message
        return "Error: Invalid input format"

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
This script uses a regular expression to extract the numbers of apples and oranges from the input string, and then calculates the number of mango fruits by subtracting these numbers from the total number of fruits. The result is returned as an integer. If the input string does not match the expected format, the function returns an error message.