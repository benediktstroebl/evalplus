```python
import re

def fruit_distribution(s, n):
    """
    Calculates the number of mango fruits in a basket given the total number of fruits,
    apples, and oranges.

    Args:
        s (str): A string containing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    num_apples, num_oranges = map(int, re.findall(r'\d+', s))

    # Calculate the total number of apples and oranges
    total_fruit_except_mango = num_apples + num_oranges

    # Return the difference between the total number of fruits and the total number of apples and oranges
    return n - total_fruit_except_mango

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses the `re` module to extract the numbers of apples and oranges from the input string using regular expressions. It then calculates the total number of apples and oranges, and returns the difference between the total number of fruits and this total.