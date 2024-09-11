```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the number of apples and oranges from the string
    pattern = r"(\d+) apples and (\d+) oranges"
    match = re.search(pattern, s)
    
    if match:
        # Extract the number of apples and oranges from the match
        apples, oranges = match.groups()
        
        # Convert the extracted numbers to integers and calculate the number of mango fruits
        return n - int(apples) - int(oranges)
    else:
        # If the string does not match the pattern, raise an exception
        raise ValueError("Invalid input string")

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))   # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))    # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```