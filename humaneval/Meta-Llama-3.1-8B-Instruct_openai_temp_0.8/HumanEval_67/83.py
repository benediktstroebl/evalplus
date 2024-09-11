```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits, 
    and the number of apples and oranges.

    Args:
        s (str): A string containing the number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.

    Example:
        fruit_distribution("5 apples and 6 oranges", 19) -> 8
        fruit_distribution("0 apples and 1 oranges",3) -> 2
        fruit_distribution("2 apples and 3 oranges", 100) -> 95
        fruit_distribution("100 apples and 1 oranges",120) -> 19
    """

    # Extract the number of apples and oranges from the string using regular expression
    apples_oranges = re.findall(r'\d+', s)

    # Ensure we have at least two numbers (apples and oranges)
    if len(apples_oranges) < 2:
        raise ValueError('Invalid input string')

    # Convert the extracted numbers to integers
    num_apples = int(apples_oranges[0])
    num_oranges = int(apples_oranges[1])

    # Calculate the number of mango fruits
    num_mango = n - num_apples - num_oranges

    return num_mango

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script works by using a regular expression to extract the numbers of apples and oranges from the input string. It then subtracts these numbers from the total number of fruits to get the number of mango fruits. If the input string does not contain exactly two numbers, it raises a ValueError.