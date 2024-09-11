```python
import re

def fruit_distribution(s, n):
    """
    Calculates the number of mango fruits in a basket given the total number of fruits, 
    apples, and oranges.

    Args:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the total number of apples and oranges
    apples, oranges = map(int, re.findall(r'\d+', s))

    # Calculate the number of mango fruits
    mangoes = n - apples - oranges

    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # 19
```

In this script, the regular expression `\d+` is used to match one or more digits in the string. The `re.findall(r'\d+', s)` function returns a list of all matches, which are then converted to integers using the `map(int,...)` function. The number of mango fruits is calculated by subtracting the total number of apples and oranges from the total number of fruits in the basket.