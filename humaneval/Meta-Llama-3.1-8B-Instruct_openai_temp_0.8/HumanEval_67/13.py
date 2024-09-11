```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    
    # Use regular expression to extract the numbers from the string
    numbers = re.findall('\d+', s)
    
    # Convert the extracted numbers to integers
    numbers = [int(num) for num in numbers]
    
    # The problem statement implies that the first number is the number of apples
    # and the second number is the number of oranges. So, subtract these from the total
    return n - sum(numbers)

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script uses regular expressions to extract the numbers from the input string. It then converts these numbers to integers and subtracts their sum from the total number of fruits to find the number of mangoes.