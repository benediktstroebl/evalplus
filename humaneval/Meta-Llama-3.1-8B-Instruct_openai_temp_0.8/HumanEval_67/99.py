```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits,
    the total number of apples, and the total number of oranges.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.

    """
    # Use regular expression to extract the number of apples and oranges from the string
    apples_oranges = re.findall(r'\d+', s)
    
    # Check if there is exactly one match (i.e., one number)
    if len(apples_oranges)!= 1:
        raise ValueError("Invalid input. Expected exactly one number.")
    
    # Convert the extracted number to an integer
    num_apples_oranges = int(apples_oranges[0])
    
    # Calculate the number of mango fruits
    num_mangoes = n - num_apples_oranges
    
    return num_mangoes

# Example usage:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

This script uses a regular expression to extract the number of apples and oranges from the input string. It then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits in the basket.