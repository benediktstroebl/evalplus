```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
    s (str): A string representing the total number of apples and oranges in a basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """

    # Use regular expression to extract the number of apples and oranges from the string
    num_apples = int(re.search(r'(\d+) apples', s).group(1))
    num_oranges = int(re.search(r'(\d+) oranges', s).group(1))

    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits
    num_mangoes = n - num_apples - num_oranges

    return num_mangoes

# Example usage:
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses regular expressions to extract the number of apples and oranges from the input string `s`. It then subtracts these numbers from the total number of fruits `n` to calculate the number of mango fruits.