```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the number of apples and oranges.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    matches = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    apples = int(matches[0])
    oranges = int(matches[1])
    
    # Return the difference between the total number of fruits and the number of apples and oranges
    return n - apples - oranges

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```
This script uses a regular expression to extract the numbers of apples and oranges from the input string, converts them to integers, and then calculates the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits.