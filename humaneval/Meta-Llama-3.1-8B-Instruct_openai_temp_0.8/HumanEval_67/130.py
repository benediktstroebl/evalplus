```python
def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket.
    
    Parameters:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Split the string into two parts: the number of apples and oranges
    apples_oranges = s.split(' and ')
    
    # Initialize total number of apples and oranges to 0
    total_apples_oranges = 0
    
    # Extract and convert the numbers to integers, then add them together
    for fruit in apples_oranges:
        # Find the number of fruits in the string
        num = int(''.join(filter(str.isdigit, fruit)))
        
        # Remove the string of fruits from the fruit string
        fruit = ''.join(filter(lambda x: not x.isdigit(), fruit))
        
        # Add the number of fruits to the total
        total_apples_oranges += num
        
    # Return the total number of fruits minus the total number of apples and oranges
    return n - total_apples_oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```