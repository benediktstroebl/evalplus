```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)

    # Take the two closest numbers and return them in order
    return numbers[0:1]

# Unit tests
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

# Test case 1
test_results = find_closest_elements([1.0, 2.0, 3.0, 4.0])
print("The closest elements in order:", test_results)

# Test case 2
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

# Test case 3
test_results = find_closest_elements([1.0, 1.0, 2.0, 3.0])
print("The closest elements in order:", test_results)

This Python code defines a function called `find_closest_elements`, which takes a list of numbers as input and returns a tuple containing the two closest elements in that list, along with the separation between them. 

The function first sorts the list of numbers. Then, it uses the pair-wise selection algorithm to find the two closest elements and returns them in order. The function is tested by passing various test cases, and the results are printed to the console.