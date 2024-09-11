```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number 
    of the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Args:
        s (str): A string that contains the number of apples and oranges.
        n (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.
    """
    matches = re.findall(r'(\d+) apples and (\d+) oranges', s)
    if matches:
        num_apples, num_oranges = map(int, matches[0])
    else:
        raise ValueError("Invalid input string. Cannot extract numbers.")

    num_mangoes = n - num_apples - num_oranges
    return max(num_mangoes, 0)

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
```

In this script, we use the `re` module to extract the numbers of apples and oranges from the string. We then subtract these numbers from the total number of fruits to get the number of mangoes. If the input string does not match the expected pattern, we raise a `ValueError`. The `max` function is used to ensure that we return 0 if the number of mangoes is negative.