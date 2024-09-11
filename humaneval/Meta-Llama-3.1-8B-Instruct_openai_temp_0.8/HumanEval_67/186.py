Here's a Python script that solves the problem:

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
    s (str): A string that represents the total number of the oranges and apples
    n (int): The total number of the fruits in the basket

    Returns:
    int: The number of mango fruits in the basket

    Example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 19
    """
    
    # Extract the numbers of apples and oranges from the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    apples = int(numbers[0])
    oranges = int(numbers[1])
    
    # Return the difference between the total number of fruits and the number of apples and oranges
    return n - apples - oranges

# Test the function with the provided examples
print(fruit_distribution("5 apples and 6 oranges", 19))  # -> 8
print(fruit_distribution("0 apples and 1 oranges", 3))    # -> 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # -> 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # -> 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string `s`. It then converts the extracted numbers to integers and returns the difference between the total number of fruits `n` and the number of apples and oranges.