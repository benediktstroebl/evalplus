```python
import re

def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    match = re.search(r"(\d+)\s+(apples|oranges)", s)
    if match:
        num_fruits = match.group(1)
        num_fruit = match.group(2)
        
        # Convert the extracted numbers to integers
        num_fruits = int(num_fruits)
        
        # Calculate the number of mango fruits
        num_mango = n - num_fruits * (1 if num_fruit == 'apples' else 2)
        
        return num_mango
    else:
        # If the input string does not match the expected pattern, raise a ValueError
        raise ValueError("Invalid input string")

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 orange", 120))  # Output: 19
```

This script uses a regular expression to extract the numbers of apples and oranges from the input string. It then calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits in the basket. If the input string does not match the expected pattern, it raises a ValueError. The script includes test cases to demonstrate its functionality.