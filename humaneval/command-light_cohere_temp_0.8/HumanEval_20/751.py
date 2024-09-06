Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Selects two numbers that are closest to each other and returns them in order (smaller number, larger number)
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    # Get the first and last numbers in the sorted list
    first_number = sorted_numbers[0]
    last_number = sorted_numbers[-1]
    # Calculate the difference between the two numbers
    difference = abs(first_number - last_number)
    # Return the two numbers and the difference
    return (first_number, last_number), difference
``` 
This function takes a list of numbers as input and returns a tuple with the two closest numbers and the difference between them. The function uses the difference between the two numbers to determine which is the smaller number. 
You can use this function with any list of numbers and it will return the two closest numbers along with the difference.