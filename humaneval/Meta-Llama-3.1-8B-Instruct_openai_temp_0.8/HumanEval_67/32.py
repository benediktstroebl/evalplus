```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits, 
    and the number of apples and oranges.

    Args:
    s (str): A string that represents a number of apples and oranges.
    n (int): An integer that represents the total number of the fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to find the numbers of apples and oranges in the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes
```

Here's an example usage of the function:

```python
# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This code uses the `re` module to find the numbers of apples and oranges in the input string using a regular expression. The numbers are extracted using `re.findall(r'\d+', s)`, which finds all sequences of digits in the string. The `map(int,...)` function is then used to convert the extracted numbers from strings to integers. Finally, the number of mango fruits is calculated by subtracting the numbers of apples and oranges from the total number of fruits.