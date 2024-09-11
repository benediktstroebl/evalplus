```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits, 
    apples, and oranges.

    Args:
        s (str): A string that represents the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    numbers = re.findall(r'\d+', s)
    apples = int(numbers[0])
    oranges = int(numbers[1])

    # Calculate the total number of apples and oranges
    total_fruit = apples + oranges

    # Return the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    return n - total_fruit

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. The string `s` represents the total number of apples and oranges, and the integer `n` represents the total number of fruits in the basket. The function uses regular expression to extract the number of apples and oranges from the string and then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits. The function returns the number of mango fruits. The script includes example use cases to demonstrate the function's behavior.