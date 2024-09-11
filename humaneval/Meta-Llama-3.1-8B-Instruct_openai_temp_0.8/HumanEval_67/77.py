```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Parameters:
    s (str): A string representing the distribution of apples and oranges.
    n (int): An integer representing the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """

    # Use regular expression to extract the numbers of apples and oranges from the string
    apples = int(re.search(r'\d+', re.sub('[^0-9]','', s)).group())
    oranges = int(re.search(r'\d+', re.sub('[^0-9]','', s)).group(2))

    # Return the difference between the total number of fruits and the number of apples and oranges
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 19 - 5 - 6 = 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 3 - 0 - 1 = 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 100 - 2 - 3 = 95
print(fruit_distribution("100 apples and 1 oranges", 120))# Output: 120 - 100 - 1 = 19
```

However, this script will only work if the input string always contains two numbers and the word "apples" and "oranges". It does not handle the case where the string might contain other numbers or words.

Here is a version of the function that uses a more robust approach:

```python
import re

def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.

    Parameters:
    s (str): A string representing the distribution of apples and oranges.
    n (int): An integer representing the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """

    # Use regular expression to find all groups of digits in the string
    numbers = [int(num) for num in re.findall(r'\d+', s)]

    # Check if the string contains exactly two numbers
    if len(numbers)!= 2:
        raise ValueError("Input string must contain exactly two numbers.")

    # Extract the numbers of apples and oranges
    apples = numbers[0]
    oranges = numbers[1]

    # Return the difference between the total number of fruits and the number of apples and oranges
    return n - apples - oranges

# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 19 - 5 - 6 = 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 3 - 0 - 1 = 2
print(fruit