```python
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the distribution of apples and oranges.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
             The string should be in the format "x apples and y oranges".
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    import re

    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+) apples and (\d+) oranges", s)
    if match:
        apples, oranges = map(int, match.groups())
    else:
        raise ValueError("Invalid input string. Please use the format 'x apples and y oranges'.")

    # Calculate the number of mango fruits
    mangoes = n - apples - oranges

    return mangoes

# Example use cases:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It uses regular expression to extract the numbers of apples and oranges from the string and then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits `n`. The function returns the calculated number of mango fruits.

The script also includes example use cases to demonstrate how to use the function.