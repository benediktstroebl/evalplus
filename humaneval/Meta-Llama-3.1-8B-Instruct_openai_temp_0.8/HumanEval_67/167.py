```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given a string that 
    represents the total number of apples and oranges and an integer that represents 
    the total number of fruits in the basket.

    Args:
        s (str): A string that represents the total number of apples and oranges.
        n (int): An integer that represents the total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Return the number of mango fruits by subtracting the number of apples and oranges from the total
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string. It then subtracts these numbers from the total number of fruits to calculate the number of mangoes.