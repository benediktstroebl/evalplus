```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers] + [100.0]
   0] * [0.0]
   _for_numbers_to_unit(numbers)
    return numbers

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(numbers)

# Test
print(numbers)

# Test 2:
def test_rescale_unit(test_case:List[float])) ->
    expected = [0.0, 0.0, 0.0, 0.0]
   -for_numbers_to_unit(test_case)
    return test_case == expected

test_rescale_unit([1.0, 2.0, 3.0, 4.0, 5.0])
rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0])
rescale_to_unit([1.0, 2.0, 3.0, 4])
test_rescale_unit([test_case])

# Test 3:
def test_rescale_unit_failed(test_case:List[float]))-> bool
    expected = [0.0, 0.0, 0.0]
   0] + [100.0] * [0.0]
   0]
   _for_numbers_to_unit(test_case)
    return test_case == expected

test_rescale_unit_failed([1.0, 2.0, 3.0, 4])
test_rescale_unit_failed([test_case])

```
This Python script defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a new list where each number has been scaled to be between 0 and 1. The function uses the list comprehension and the `numbers_to_unit` function from the `typing` module to achieve this. 

The `test_rescale_unit` function tests the `rescale_to_unit` function by passing a test case (a list of numbers) and comparing the resulting list with the expected output. 

The `test_rescale_unit_failed` function tests the `rescale_to_unit` function by passing a test case and checking if the function returns `True`.  The output of the test cases is printed to the console.