Here's a self-contained Python script that solves the problem:
```markdown
### Fruit Distribution Problem

#### Solution

```python
def fruit_distribution(s, n):
    """
    Returns the number of mango fruits in the basket.
    
    Parameters:
    s (str): A string that represents a number of apples and oranges.
    n (int): An integer that represents the total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    
    # Use regular expressions to extract the numbers of apples and oranges from the string
    import re
    apples, oranges = map(int, re.findall(r'\d+', s))
    
    # Calculate the total number of apples and oranges
    total_fruit = apples + oranges
    
    # Return the number of mango fruits
    return n - total_fruit

# Example use cases:
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

#### Explanation

This script uses a regular expression to extract the numbers of apples and oranges from the input string. The `map` function is then used to convert these numbers to integers. The total number of apples and oranges is calculated by adding these two numbers together. Finally, the number of mango fruits is calculated by subtracting the total number of apples and oranges from the total number of fruits in the basket.