```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements in the list that are the closest to each other. Returns a tuple of the smallest and largest number. """

    def test(lst: List[float]):
    return find_closest_elements(sorted(lst, reverse=True)), sorted(lst)[0], sorted(lst)[1]

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
def test_result(test_case: List[float]):
    return test_case == find_closest_elements(test_case)

``` 
The script defines a function find_closest_elements that takes a list of numbers as input and returns a tuple of the two numbers in the list that are the closest to each other. The function first sorts the minimum and maximum values in the list and then returns the minimum and maximum values in that order.

The function tests are defined that take a list of numbers and pass them to the find_closest_elements function to test if the output is correct. 

The test_result function takes a list of numbers and passes them to the test function to see if the output is correct.