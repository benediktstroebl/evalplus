```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Parameters:
    s (str): A string that represents the total number of oranges and apples.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers from the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    numbers = [int(num) for num in numbers]
    
    # The first two numbers in the list represent the number of apples and oranges
    apples = numbers[0]
    oranges = numbers[1]
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

In this script, we use a regular expression to extract the numbers from the input string. We then convert these numbers to integers, calculate the number of mango fruits, and return the result. The function is tested with the provided examples.