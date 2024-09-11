```python
import re

def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Use regular expression to extract the numbers of apples and oranges
    apples_oranges = re.findall(r'\d+', s)
    
    # Extract the numbers of apples and oranges
    apples = int(apples_oranges[0])
    oranges = int(apples_oranges[1])

    # Calculate the total number of fruits excluding apples and oranges
    total_mango = n - apples - oranges
    
    return total_mango

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges",3))  # 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # 95
print(fruit_distribution("100 apples and 1 oranges",120))  # 19
```

In this script, the `fruit_distribution` function uses a regular expression to extract the numbers of apples and oranges from the input string `s`. It then subtracts these numbers from the total number of fruits `n` to get the number of mango fruits. The test cases at the end of the script demonstrate the function's correctness.