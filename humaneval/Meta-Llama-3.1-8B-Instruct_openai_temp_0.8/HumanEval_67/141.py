```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers from the string
    pattern = r"(\d+)"
    numbers = list(map(int, re.findall(pattern, s)))
    
    # Calculate the total number of apples and oranges
    total_apples_oranges = sum(numbers)
    
    # Calculate the number of mango fruits
    mango_fruits = n - total_apples_oranges
    
    return mango_fruits

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # 19
```

This script uses a regular expression to extract numbers from the input string. It then calculates the total number of apples and oranges, and finally returns the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits in the basket.