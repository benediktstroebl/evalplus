### Fruit Distribution Calculator

The following Python script solves the problem by parsing the input string to extract the number of apples and oranges, then subtracts these from the total number of fruits to find the number of mangoes.

```python
import re

def fruit_distribution(s, n):
    """
    Calculates the number of mangoes in a basket given the total number of fruits,
    and a string describing the number of apples and oranges.

    Args:
        s (str): A string describing the number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mangoes in the basket.
    """

    # Use regular expressions to extract the number of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))

    # Subtract the number of apples and oranges from the total number of fruits
    return n - apples - oranges

# Example use cases:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses the `re` module to parse the input string and extract the numbers of apples and oranges. It then subtracts these from the total number of fruits to find the number of mangoes.