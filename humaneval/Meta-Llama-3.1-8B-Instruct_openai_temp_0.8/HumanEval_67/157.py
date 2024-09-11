### Fruit Distribution Script
```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expressions to extract the number of apples and oranges
    apples = re.findall(r'\d+ apples', s)[0][:-7]
    oranges = re.findall(r'\b\d+ oranges', s)[0][:-8]

    # Calculate the total number of apples and oranges
    total_fruit = int(apples) + int(oranges)

    # Return the number of mango fruits
    return n - total_fruit

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```
This script uses regular expressions to extract the number of apples and oranges from the input string `s`. It then calculates the total number of fruit and returns the number of mango fruits by subtracting the total number of fruit from the input `n`.