```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Args:
        s (str): A string that represents the total number of the oranges and apples 
                 and an integer that represent the total number of the fruits in the basket.
        n (int): The total number of the fruits in the basket.

    Returns:
        int: The number of the mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the numbers to integers
    num_apples = int(numbers[0])
    num_oranges = int(numbers[1])
    
    # Return the total number of fruits minus the number of apples and oranges
    return n - num_apples - num_oranges

# Test the function with examples
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```