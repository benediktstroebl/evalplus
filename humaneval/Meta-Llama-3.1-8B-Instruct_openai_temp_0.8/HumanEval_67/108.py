### Fruit Distribution Script
```markdown
### Problem: Calculate the number of mango fruits in a basket given the distribution of apples and oranges.

### Solution
```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given the distribution of apples and oranges.

    Args:
    s (str): A string that represents a number of apples and oranges in a basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.

    Example:
    fruit_distribution("5 apples and 6 oranges", 19) -> 8
    fruit_distribution("0 apples and 1 oranges", 3) -> 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 95
    fruit_distribution("100 apples and 1 oranges", 120) -> 19
    """
    # Use regular expression to extract the numbers of apples and oranges from the string
    matches = re.findall(r'\d+', s)
    
    # Convert the matches to integers and calculate the total number of apples and oranges
    total_apples_oranges = sum(map(int, matches))
    
    # Calculate the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    total_mango = n - total_apples_oranges
    
    return total_mango

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # 19
```
This script uses a regular expression to extract the numbers of apples and oranges from the input string, calculates the total number of apples and oranges, and then subtracts this total from the total number of fruits to find the number of mango fruits.