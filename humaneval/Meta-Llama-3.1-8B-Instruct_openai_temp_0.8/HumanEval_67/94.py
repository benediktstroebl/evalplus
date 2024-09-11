```python
import re

def fruit_distribution(s, n):
    """
    This function takes a string representing the total number of apples and oranges in a basket,
    and an integer representing the total number of fruits in the basket. It returns the number of mangoes.

    Parameters:
    s (str): A string containing the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mangoes in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the total number of apples and oranges
    total_fruit = apples + oranges
    
    # Return the difference between the total number of fruits and the total number of apples and oranges
    return n - total_fruit

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # -> 8
print(fruit_distribution("0 apples and 1 oranges",3)) # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # -> 95
print(fruit_distribution("100 apples and 1 oranges",120)) # -> 19
```

This script uses the `re` module to extract the numbers of apples and oranges from the input string using regular expressions. It then calculates the total number of fruits and returns the difference between the total number of fruits and the total number of apples and oranges.