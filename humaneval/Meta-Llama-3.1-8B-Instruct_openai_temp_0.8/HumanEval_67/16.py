```python
import re

def fruit_distribution(s, n):
    """
    This function calculates the number of mango fruits in a basket given the total number of fruits,
    and the number of apples and oranges.

    Parameters:
    s (str): A string that represents the total number of apples and oranges.
    n (int): An integer that represents the total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """

    # Use regular expression to extract the number of apples and oranges from the string
    apples_oranges = re.findall(r'\d+', s)
    
    # Check if the string contains information about apples and oranges
    if len(apples_oranges) == 2:
        # Convert the extracted numbers to integers
        num_apples = int(apples_oranges[0])
        num_oranges = int(apples_oranges[1].replace(' oranges', '').replace(' apples', ''))
        
        # Return the total number of fruits minus the number of apples and oranges
        return n - num_apples - num_oranges
    else:
        # If the string does not contain information about apples and oranges, return the total number of fruits
        return n

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Expected output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Expected output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Expected output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Expected output: 19
```
This script first uses regular expression to extract the numbers of apples and oranges from the input string. It then converts these numbers to integers and subtracts them from the total number of fruits to calculate the number of mango fruits. If the input string does not contain information about apples and oranges, it simply returns the total number of fruits. The test cases at the end demonstrate the function's correctness.