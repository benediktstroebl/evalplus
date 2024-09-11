```python
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Args:
    s (str): A string representing the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Split the input string into two parts at the word "and"
    parts = s.split(" and ")
    
    # Initialize variables to store the number of apples and oranges
    apples = 0
    oranges = 0
    
    # Iterate over each part to extract the number of apples and oranges
    for part in parts:
        # Split the part into two numbers and a fruit type
        num_and_fruit = part.split()
        
        # Extract the number
        num = int(num_and_fruit[0])
        
        # Check which fruit type is mentioned
        if num_and_fruit[1] == "apples":
            apples = num
        elif num_and_fruit[1] == "oranges":
            oranges = num
    
    # Calculate and return the number of mango fruits
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```