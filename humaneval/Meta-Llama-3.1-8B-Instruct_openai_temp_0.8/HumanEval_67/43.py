### Fruit Distribution Script
```markdown
# Define a function to calculate the number of mango fruits
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket given a string representation of the number of apples and oranges and the total number of fruits.

    Args:
        s (str): A string representing the number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Split the input string into a list of strings
    fruits = s.split()
    
    # Initialize variables to store the number of apples and oranges
    apples = 0
    oranges = 0
    
    # Iterate over the list to find the number of apples and oranges
    for i in range(len(fruits)):
        # Check if the string represents a number of fruits
        if fruits[i].isdigit():
            # Convert the string to an integer and store it in the corresponding variable
            if i % 2 == 0:
                oranges = int(fruits[i])
            else:
                apples = int(fruits[i])
    
    # Calculate the number of mango fruits and return the result
    return n - apples - oranges

# Example usage:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```