```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Parameters:
    s (str): A string that represents the total number of apples and oranges.
    n (int): An integer that represents the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    num_apples = int(re.search(r'(\d+) apples', s).group(1))
    num_oranges = int(re.search(r'(\d+) oranges', s).group(1))
    
    # Return the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits
    return n - num_apples - num_oranges

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))    # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))     # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))   # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

In this script, we use the `re` module to extract the number of apples and oranges from the input string `s` using regular expressions. We then simply subtract the number of apples and oranges from the total number of fruits `n` to get the number of mango fruits.