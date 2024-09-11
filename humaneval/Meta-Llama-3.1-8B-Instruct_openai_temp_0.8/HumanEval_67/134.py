```python
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string that represents a number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Split the input string into two parts at the word 'oranges' and extract the number of oranges
    oranges = int(s.split('oranges')[0].split('and')[-1].split(' ')[-1])
    
    # Extract the number of apples from the string
    apples = int(s.split('apples')[0].split('and')[-1].split(' ')[-1])
    
    # Calculate the total number of fruits that are not mangoes
    non_mango_fruits = oranges + apples
    
    # Return the number of mango fruits by subtracting the non-mango fruits from the total number of fruits
    return n - non_mango_fruits

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # ->19 - 5 - 6 = 8
print(fruit_distribution("0 apples and 1 oranges",3))  # -> 3 - 0 - 1 = 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # -> 100 - 2 - 3 = 95
print(fruit_distribution("100 apples and 1 oranges",120))  # -> 120 - 100 - 1 = 19
```

This Python script defines a function `fruit_distribution` that takes a string `s` representing the number of apples and oranges and an integer `n` representing the total number of fruits in the basket. It then extracts the numbers of apples and oranges from the string, calculates the total number of non-mango fruits, and returns the number of mango fruits by subtracting the non-mango fruits from the total number of fruits. The script also includes four test cases to demonstrate the function's correctness.