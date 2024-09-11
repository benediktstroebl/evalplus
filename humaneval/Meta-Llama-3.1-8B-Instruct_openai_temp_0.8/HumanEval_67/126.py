```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket given the string that represents 
    the total number of the oranges and apples and an integer that represent the total 
    number of the fruits in the basket.

    Args:
    s (str): A string that represents a number of apples and oranges. 
             The string should be in the format: "N apples and M oranges".
    n (int): The total number of the fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    matches = re.search(r"(\d+)\s*apples\s*and\s*(\d+)\s*oranges", s, re.IGNORECASE)
    if matches:
        # Extract the number of apples and oranges from the regular expression match
        num_apples = int(matches.group(1))
        num_oranges = int(matches.group(2))
        # Return the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits
        return n - num_apples - num_oranges
    else:
        raise ValueError("Invalid input string. Please use the format: 'N apples and M oranges'.")

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

In this code, we use the `re` module to extract the number of apples and oranges from the input string using regular expressions. If the input string is in the correct format, we extract the numbers using `re.search` and then return the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits. If the input string is not in the correct format, we raise a `ValueError`.