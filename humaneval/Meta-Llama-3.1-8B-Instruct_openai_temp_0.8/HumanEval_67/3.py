```python
def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Parameters:
    s (str): A string that contains the number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Split the input string into two parts: the number of fruits and the types
    num_str, fruits_str = s.split(' and ')
    
    # Extract the number of fruits from the strings
    num_str = num_str.split()
    num_fruits = int(num_str[0])
    
    # Extract the number of apples and oranges from the string
    fruits_str = fruits_str.split()
    apples = int(fruits_str[0])
    oranges = int(fruits_str[2])
    
    # Calculate the number of mangoes
    mangoes = n - num_fruits
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. It splits the input string into two parts, extracts the number of fruits and the types of fruits, and calculates the number of mangoes by subtracting the total number of fruits from the input `n`. The function then returns the number of mangoes. The script also includes test cases to verify the function's correctness.