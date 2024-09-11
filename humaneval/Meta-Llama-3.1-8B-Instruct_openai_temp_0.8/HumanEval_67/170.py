### Fruit Distribution Script
```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket, given the total number of fruits
    and the distribution of apples and oranges.

    Args:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the total number of apples and oranges
    apples_oranges = re.findall(r'\d+', s)
    # Convert the extracted numbers to integers and sum them
    total_apples_oranges = sum(map(int, apples_oranges))
    # Return the total number of fruits minus the apples and oranges
    return n - total_apples_oranges

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```
This script uses the `re` module to extract the total number of apples and oranges from the input string `s`. It then converts the extracted numbers to integers and sums them. Finally, it returns the total number of fruits in the basket minus the sum of apples and oranges.