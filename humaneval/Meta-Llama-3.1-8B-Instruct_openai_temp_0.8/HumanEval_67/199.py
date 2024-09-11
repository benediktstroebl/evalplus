```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Args:
    s (str): A string containing the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    apples = int(re.search(r'\d+ apples', s).group().split(' ')[0])
    oranges = int(re.search(r'\d+ oranges', s).group().split(' ')[0])
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    mangoes = n - apples - oranges
    
    return mangoes

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script defines a function `fruit_distribution` that uses regular expressions to extract the number of apples and oranges from the input string. It then calculates the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits. The example use cases demonstrate the function's behavior with different inputs.