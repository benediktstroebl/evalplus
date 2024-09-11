```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mangoes in a fruit basket.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mangoes in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
This script uses the `re` module to extract the numbers of apples and oranges from the string using a regular expression. It then calculates the number of mangoes by subtracting the numbers of apples and oranges from the total number of fruits.