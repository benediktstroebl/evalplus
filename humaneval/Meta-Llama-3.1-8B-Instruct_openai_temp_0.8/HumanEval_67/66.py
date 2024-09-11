```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
        s (str): A string that represents a number of apples and oranges.
        n (int): An integer that represents the total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This Python script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. The string `s` represents the number of apples and oranges in the basket, and the integer `n` represents the total number of fruits in the basket. The function uses regular expression to extract the numbers of apples and oranges from the string, and then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits. The function returns the number of mango fruits. The script also includes test cases to demonstrate the function's correctness.