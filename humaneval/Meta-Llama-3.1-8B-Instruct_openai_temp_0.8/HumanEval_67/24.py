Here's a Python script that uses regular expressions to extract the number of apples and oranges from the input string and then calculates the number of mangoes:
```markdown
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mangoes given the string that represents the total number of 
    the oranges and apples and an integer that represents the total number of the fruits 
    in the basket.

    Args:
        s (str): A string that represents a number of apples and oranges 
                 distributed in a basket of fruit.
        n (int): An integer that represent the total number of the fruits 
                 in the basket.

    Returns:
        int: The number of the mango fruits in the basket.
    """
    # Extract the number of apples and oranges using regular expressions
    match = re.search(r'(\d+) apples and (\d+) oranges', s)
    
    # If the regular expression matches, extract the numbers
    if match:
        apples = int(match.group(1))
        oranges = int(match.group(2))
        
        # Calculate the number of mangoes
        mangoes = n - apples - oranges
        return mangoes
    else:
        # If the regular expression does not match, raise an exception
        raise ValueError("Invalid input format")

# Example usage
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
This script uses a regular expression to extract the numbers from the input string, and then calculates the number of mangoes by subtracting the number of apples and oranges from the total number of fruits. If the input format does not match the regular expression, it raises a ValueError.