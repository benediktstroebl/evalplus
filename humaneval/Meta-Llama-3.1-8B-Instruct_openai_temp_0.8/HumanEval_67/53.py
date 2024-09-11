```python
import re

def fruit_distribution(s, total_fruits):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges in the basket.
    total_fruits (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    mangoes = total_fruits - apples - oranges
    
    return mangoes

# Test the function with example inputs
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))# Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `total_fruits` as input. It uses regular expression to extract the number of apples and oranges from the string, and then calculates the number of mango fruits by subtracting the number of apples and oranges from the total. The function then returns the number of mango fruits. The script also includes test cases to demonstrate the function's correctness.