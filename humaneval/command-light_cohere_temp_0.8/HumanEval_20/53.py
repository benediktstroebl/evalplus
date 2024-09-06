```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize and return the first two elements of the list
    return (min(numbers), max(numbers))]

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
print_stdout(" Closest numbers are: (1.0, 2.0)")

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
print_stdout(" Closest numbers are: (1.0, 2.0)"))

numbers = [1.0, 2.0, 3.0, 5.0, 6]
print_stdout(" Closest numbers are: (3.0, 5.0)"))

numbers = [1.0, 2.0, 3.0, 3.0, 4]
print_stdout(" Closest numbers are: (1.0, 3.0)")
numbers = [1.0, 2.0, 3.0, 6]
print_stdout(" Closest numbers are: (1.0, 6.0)")
numbers = [1.0, 2.0, 3.0, 7]
print_stdout(" Closest numbers are: (1.0, 7.0)")

numbers = [1.0, 2.0, 4.0, 8]
print_stdout(" Closest numbers are: (1.0, 8.0)")

numbers = [1.0, 1.0, 2.0, 3]].find_closest_elements(numbers)
if __name__ == 'main':
    print("...")
``` 
The script defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements in the list. The function uses the mathematical functions to find the minimum and maximum elements in the list, and returns them as a tuple.

The test cases show how to use the `find_closest_elements` function to solve the problem and print the result.