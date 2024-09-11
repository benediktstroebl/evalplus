```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket.
    
    Parameters:
    s (str): A string that represents a number of apples and oranges distributed in a basket.
    n (int): The total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function with example inputs
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This Python script uses regular expressions to extract the numbers of apples and oranges from the input string, then calculates the number of mango fruits by subtracting these numbers from the total number of fruits. The result is returned as an integer.