```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
    s (str): A string that represents the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to find the number of apples and oranges
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the total number of apples and oranges
    total_fruits = apples + oranges
    
    # Return the number of mango fruits
    return n - total_fruits

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges", 3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges", 120))
```

This script uses regular expressions to extract the numbers of apples and oranges from the input string `s`. It then calculates the total number of apples and oranges and subtracts this from the total number of fruits in the basket `n` to get the number of mango fruits. The function returns this result.