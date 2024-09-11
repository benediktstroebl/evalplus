```python
def fruit_distribution(fruit_description, total_fruits):
    """
    Calculate the number of mango fruits in a basket given the total number of fruits,
    apples, and oranges.

    Args:
        fruit_description (str): A string describing the number of apples and oranges.
        total_fruits (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    # Split the string into words and count the number of apples and oranges
    words = fruit_description.split()
    apples = int(words[0])
    oranges = int(words[-2])

    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    mangoes = total_fruits - apples - oranges

    return mangoes

# Test the function with example inputs
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```
In this script, we first split the input string into words using the `split()` method. We then count the number of apples and oranges by converting the corresponding words to integers using `int()`. Finally, we calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits. The result is returned as an integer.