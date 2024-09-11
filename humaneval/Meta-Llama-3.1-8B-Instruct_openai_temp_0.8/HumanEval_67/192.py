### Mango Fruit Distribution
#### A Python Script to Calculate the Number of Mango Fruits

```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Args:
    s (str): A string representing the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges
    numbers = re.findall('\d+', s)
    apples = int(numbers[0])
    oranges = int(numbers[1])

    # Calculate the number of mango fruits
    mangoes = n - apples - oranges

    return mangoes

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the number of apples and oranges from the input string. It then calculates the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits. The result is returned as an integer.