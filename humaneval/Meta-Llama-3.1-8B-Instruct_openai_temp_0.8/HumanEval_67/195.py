```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits, 
    apples, and oranges in the basket.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers and calculate the total number of apples and oranges
    apples = int(numbers[0])
    oranges = int(numbers[1])
    
    # Subtract the total number of apples and oranges from the total number of fruits to get the number of mangoes
    mangoes = n - apples - oranges
    
    return mangoes

# Test the function with the provided examples
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
print(fruit_distribution("0 apples and 1 oranges",3)) # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges",120)) # Output: 19
```