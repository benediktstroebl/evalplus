### Fruit Distribution Problem
#### Python Solution
```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket.

    Parameters:
    s (str): A string that represents the total number of apples and oranges.
    n (int): An integer that represents the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges
    numbers = re.findall(r'\d+', s)
    
    # Get the number of apples and oranges from the list of numbers
    apples, oranges = map(int, numbers)
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```
This Python script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It uses regular expressions to extract the number of apples and oranges from the string, and then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits. The script includes example test cases to demonstrate the function's functionality.