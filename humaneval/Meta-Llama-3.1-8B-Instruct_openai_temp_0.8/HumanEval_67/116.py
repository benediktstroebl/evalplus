### Fruit Distribution Problem
#### A Python Script to Calculate the Number of Mango Fruits in a Basket

```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string that represents the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    apples_oranges = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    apples = int(apples_oranges[0])
    oranges = int(apples_oranges[1])
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    
    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses the `re` module's `findall` function to extract the numbers from the input string using a regular expression. The extracted numbers are then converted to integers and used to calculate the number of mango fruits. The result is returned by the `fruit_distribution` function.