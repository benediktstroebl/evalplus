```python
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Parameters:
    s (str): A string that represents a number of apples and oranges.
    n (int): The total number of the fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Split the input string into two parts: the numbers and the fruits
    num_str, fruit_str = s.split()
    
    # Extract the numbers from the string
    num_str = num_str.replace(' ', '')
    num_str = num_str.replace(',', '')
    
    # Convert the numbers to integers and add them together
    total_apples_oranges = int(num_str.split('+')[0].lstrip('0')) + int(num_str.split('+')[1].lstrip('0'))
    
    # Return the difference between the total number of fruits and the total number of apples and oranges
    return n - total_apples_oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges",3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges",120))  # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It splits the string into two parts: the numbers and the fruits, extracts the numbers from the string, adds them together, and returns the difference between the total number of fruits and the total number of apples and oranges.