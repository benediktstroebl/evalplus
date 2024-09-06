Here is a self-contained Python script that solves the problem of checking if any two numbers in a list are closer than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # Sort the list of numbers
    numbers = sorted(numbers)
    
    # Initialize two variables, index of smaller number and index of larger number
    smaller_index = 0
    larger_index = 0
    
    # Loop through the list of numbers
    for i in range(1, len(numbers)):
        # Compare the current number with the previous one
        if numbers[i] < numbers[smaller_index]:
            smaller_index = i
        elif numbers[i] > numbers[larger_index]:
            larger_index = i
            
    # If two numbers are found that are closer than the given threshold
    return smaller_index != larger_index

# Example usage
numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 2.0]


threshold = 0.3

if has_close_elements(numbers, threshold):
    print("Yes")
else:
    print("No")
```
This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns a boolean value indicating whether any two numbers in the list are closer than the given threshold. 

The function sorts the list of numbers and uses two variables, `smaller_index` and `larger_index`, to keep track of the smaller and larger numbers, respectively. It then loops through the loop, comparing each number with the previous one, and if a number is smaller than the current smaller_index, or if a number is larger than the current larger_index, then the respective index is updated.

Finally, the function returns `smaller_index != larger_index`, which is true if two numbers in the list are closer than the given threshold, and false otherwise.