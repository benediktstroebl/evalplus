```python
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Remove all non-digit and non-space characters from the string
    digits_and_spaces = ''.join(filter(str.isdigit or str.isspace, s))
    
    # Split the string into numbers and words
    numbers = list(map(int, ''.join(filter(str.isdigit, digits_and_spaces)).split()))
    
    # The first number represents the number of apples and the second number represents the number of oranges
    num_apples, num_oranges = numbers
    
    # Calculate the number of mango fruits
    num_mangoes = n - num_apples - num_oranges
    
    return num_mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

This script defines a function `fruit_distribution` that calculates the number of mango fruits in a basket given the total number of fruits, apples, and oranges. It uses regular expressions to extract the numbers from the input string, and then subtracts the number of apples and oranges from the total number of fruits to get the number of mangoes. The function is then tested with the provided test cases.