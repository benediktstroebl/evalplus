```python
import re

def fruit_distribution(s, total_fruits):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits 
    and the distribution of apples and oranges.

    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    total_fruits (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers of apples and oranges from the string
    num_apples_oranges = re.findall(r'\d+', s)
    
    # Ensure we have exactly two numbers extracted (apples and oranges)
    if len(num_apples_oranges)!= 2:
        raise ValueError("Invalid input string. Expected format: 'X apples and Y oranges'")
    
    # Convert the extracted numbers to integers
    num_apples, num_oranges = map(int, num_apples_oranges)
    
    # Calculate the number of mango fruits
    num_mangoes = total_fruits - num_apples - num_oranges
    
    return num_mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # 19
```
This script uses regular expressions to extract the numbers of apples and oranges from the input string. It then calculates the number of mango fruits by subtracting the numbers of apples and oranges from the total number of fruits. If the input string is not in the expected format, it raises a ValueError.