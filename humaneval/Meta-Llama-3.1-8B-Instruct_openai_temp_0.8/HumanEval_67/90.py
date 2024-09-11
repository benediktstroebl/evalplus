```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits
    and the distribution of apples and oranges.

    Args:
    s (str): A string representing the distribution of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """

    # Use regular expression to extract the numbers of apples and oranges from the string
    num_apples, num_oranges = map(int, re.findall(r'\d+', s))

    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    num_mango = n - num_apples - num_oranges

    return num_mango

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # -> 19
```

In this script, we use regular expressions to extract the numbers of apples and oranges from the input string `s`. We then calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits `n`.