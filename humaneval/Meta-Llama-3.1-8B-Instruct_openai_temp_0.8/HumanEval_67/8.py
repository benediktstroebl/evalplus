### Fruit Distribution Calculator

```python
import re

def fruit_distribution(fruit_string, total_fruits):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits,
    and a string representing the number of apples and oranges.

    Args:
        fruit_string (str): A string containing the number of apples and oranges.
        total_fruits (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the number of apples and oranges from the string
    match = re.search(r'(\d+)\s+(apples|oranges)', fruit_string)
    
    if match:
        # Extract the number of apples or oranges from the match
        num_apples_or_oranges = int(match.group(1))
        
        # Remove the corresponding string ('apples' or 'oranges') from the total_fruits string
        num_mangoes = total_fruits - num_apples_or_oranges - (fruit_string.split(' ')[-1] == 'oranges')
        return num_mangoes
    else:
        return "Invalid fruit string format"

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # 19
```

This script defines a function `fruit_distribution` that takes a string `fruit_string` and an integer `total_fruits` as input, and returns the number of mango fruits in the basket. The function uses regular expressions to extract the number of apples and oranges from the input string, and then calculates the number of mangoes by subtracting the total number of apples and oranges from the total number of fruits.