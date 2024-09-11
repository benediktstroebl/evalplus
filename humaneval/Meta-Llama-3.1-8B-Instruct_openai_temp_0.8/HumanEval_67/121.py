```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits and the number of apples and oranges.

    Args:
    s (str): A string representing the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.

    """
    # Use regular expression to extract the number of apples and oranges from the string
    num_apples = int(re.search(r'\d+(?= apples)', s).group())
    num_oranges = int(re.search(r'\d+(?= oranges)', s).group())

    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits
    num_mango = n - num_apples - num_oranges

    return num_mango

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It uses regular expressions to extract the number of apples and oranges from the string `s` and then calculates the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits `n`. The function returns the number of mango fruits. The script also includes test cases to demonstrate the function's correctness.