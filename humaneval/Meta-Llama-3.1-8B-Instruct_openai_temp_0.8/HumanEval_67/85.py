```python
import re

def fruit_distribution(s, n):
    """
    Calculates the number of mango fruits in a basket given the total number of fruits and a string representing the number of apples and oranges.

    Args:
        s (str): A string representing the total number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.

    Example:
        fruit_distribution("5 apples and 6 oranges", 19) -> 8
        fruit_distribution("0 apples and 1 oranges", 3) -> 2
        fruit_distribution("2 apples and 3 oranges", 100) -> 95
        fruit_distribution("100 apples and 1 oranges", 120) -> 19
    """
    # Use regular expression to extract the number of apples and oranges from the string
    apples_oranges = re.findall(r'\d+', s)
    
    # Convert the extracted numbers to integers
    apples_oranges = [int(num) for num in apples_oranges]
    
    # Extract the number of apples from the list of extracted numbers
    apples = apples_oranges[0]
    
    # If there are more than one extracted numbers, extract the number of oranges from the list
    if len(apples_oranges) > 1:
        oranges = apples_oranges[1]
    else:
        oranges = 0
    
    # Calculate the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits
    mango_fruits = n - apples - oranges
    
    return mango_fruits

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```