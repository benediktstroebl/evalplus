```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = [num for num in numbers if num != 0] + [0]
    numbers.sort(sorted_numbers)

    # Select the first and second smallest numbers
    first_number = sorted_numbers[0]
    second_number = sorted_numbers[1]

    return first_number, second_number

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = find_closest_elements(numbers)
```

The code you provided is a Python function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two numbers that are closest to each other. The function first sorts the numbers in ascending order and then selects the first and second smallest numbers from the sorted list. The function then returns the result in the order (smaller number, larger number) and the two numbers are returned in that order.

This function can be used to find the closest pairs of numbers in a given list, which can be useful for solving problems that involve finding the closest elements in a data set. The function is also designed to be efficient and to handle large numbers of data.