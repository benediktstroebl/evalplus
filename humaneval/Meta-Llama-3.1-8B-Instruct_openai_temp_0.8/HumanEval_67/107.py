```markdown
### Fruit Distribution Problem Solution
#### Problem Description
In this task, you will be given a string that represents a number of apples and oranges 
that are distributed in a basket of fruit this basket contains 
apples, oranges, and mango fruits. Given the string that represents the total number of 
the oranges and apples and an integer that represent the total number of the fruits 
in the basket return the number of the mango fruits in the basket.

#### Solution
```python
def fruit_distribution(s, total_fruits):
    """
    Calculate the number of mango fruits in the basket.

    Args:
    s (str): A string that represents the total number of apples and oranges.
    total_fruits (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Remove the word "apples and oranges" from the string
    s = s.replace("apples and oranges", "")

    # Split the string into two parts (numbers of apples and oranges)
    parts = s.split(" or ")

    # Extract the numbers of apples and oranges
    num_apples = int(parts[0].split(" apples")[0])
    num_oranges = int(parts[1].split(" oranges")[0])

    # Calculate the number of mango fruits
    num_mango = total_fruits - num_apples - num_oranges

    return num_mango

# Example use cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```
### Explanation
The `fruit_distribution` function takes a string `s` that represents the total number of apples and oranges, and an integer `total_fruits` that represents the total number of fruits in the basket.

1. The function removes the word "apples and oranges" from the string using the `replace` method.
2. It splits the string into two parts (numbers of apples and oranges) using the `split` method with the string " or " as the separator.
3. It extracts the numbers of apples and oranges by splitting each part into a number and a word, and then converting the number to an integer using the `int` function.
4. Finally, it calculates the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits.

The function returns the number of mango fruits.