Here is a Python script that includes a self-contained function to solve the problem:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # Initialize a dictionary to keep track of the elements encountered so far
    element_close_dict = {}

    # Sort the list in ascending order of numbers
    sorted_numbers = sorted(numbers)

    # Start from the end of the list
    for i in range(len(sorted_numbers) - 1, -1, -len(sorted_numbers)):
        current_num = sorted_numbers[i]
        next_num = sorted_numbers[i+1]

        # Check if the current number is less than the next number
        if current_num < next_num:
            # If so, these numbers are not close enough
            return False

        # Check if the current number is in the dictionary
        if current_num in element_close_dict:
            # If so, check if the next number is also in the dictionary
            if next_num in element_close_dict:
                # If so, return True, indicating these numbers are close enough
                return True

        # Add the current number to the dictionary
        element_close_dict[current_num] = next_num

        # Return True, indicating all numbers are close enough
        return True
```
This function takes two parameters: numbers, which is a list of float numbers, and threshold, which is a float number. The function checks if in the given list of numbers, are any two numbers closer to each other than the given threshold.  The return True, indicating all numbers are close enough.