```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the number of apples and oranges, 
    and the total number of fruits in the basket.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """

    # Use regular expression to extract the numbers of apples and oranges from the string
    pattern = r"(\d+)\s*(?:apples|oranges)"
    matches = re.findall(pattern, s)

    if len(matches)!= 2:
        raise ValueError("Invalid input string")

    # Extract the numbers of apples and oranges
    apples, oranges = [int(match) for match in matches]

    # Calculate the number of mango fruits
    mangoes = n - apples - oranges

    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It uses a regular expression to extract the numbers of apples and oranges from the string, and then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits `n`. The function returns the number of mango fruits. The script also includes test cases to demonstrate the function's correctness.