```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to find the number of apples and oranges in the string
    numbers = list(map(int, re.findall(r'\d+', s)))
    
    # The total number of apples and oranges is the sum of the first two numbers
    total_apples_oranges = sum(numbers[:2])
    
    # Calculate the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    return n - total_apples_oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

In this solution, we use the `re.findall` function from the `re` module to find all numbers in the string `s` using a regular expression. The regular expression `\d+` matches one or more digits. The `list(map(int,...))` expression converts the found numbers from strings to integers. We then sum the first two numbers to get the total number of apples and oranges. Finally, we subtract this total from the total number of fruits `n` to get the number of mango fruits.