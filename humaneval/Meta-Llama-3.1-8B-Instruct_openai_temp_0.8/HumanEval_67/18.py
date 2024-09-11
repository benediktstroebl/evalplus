```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Args:
        s (str): A string that represents a number of apples and oranges.
        n (int): The total number of the fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to find the numbers of apples and oranges in the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This Python script uses a regular expression to extract the numbers of apples and oranges from the input string `s`. It then calculates the number of mangoes by subtracting the numbers of apples and oranges from the total number of fruits `n`. The result is then returned by the function.