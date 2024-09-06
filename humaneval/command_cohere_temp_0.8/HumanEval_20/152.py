```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must be of length at least two")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return (left, right) if left != right else (left, left)
```
The function `find_closest_elements()` takes a list of numbers `numbers` as input. It first sorts the list and checks if the length is at least 2 to ensure there are enough numbers to select from and handle the edge case where the list contains only one number or is empty. It then selects the middle numbers from the sorted list and compares them. If the selected numbers are equal, it returns them in either order, if they are not, it also returns them in either order, ensuring the smaller number comes first. The function handles the edge case where the list length is less than 2, throwing an IndexError. 

Here is a simple test suite that can be used to verify the function:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 11.0, 12.0, 13.0, 14.0, 25.0, 30.0]) == (10.0, 10.0)
    assert find_closest_elements([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]) == (1.0, 2.0)
    assert find_closest_elements([10.95, 10.90, 10.80, 10.85, 10.92, 11.05, 11.10, 11.02, 11.08, 11.00, 11.07]) == (10.90, 11.00)
```

This test suite contains several test cases that cover the main scenarios and edge cases for the `find_closest_elements()` function. Each test case asserts that the function returns the expected result for the given input list of numbers.  If you use this for testing your function, you might have to adapt the `assert` statements to fit the testing framework of your choice (e.g. `TestCase` in Python's `unittest` if you are using structured testing). 

The test cases cover the following scenarios:
- Test case `test_find_closest_elements()` verifies that the function works correctly when the list contains only two unique elements and they are equal to each other.
- Test case `test_find_closest_elements()` verifies that the function selects the smallest and largest elements when the list contains integers between 1 and 10.
- Test case `test_find_closest_elements()` verifies that the function selects the smallest and second-smallest elements when the list contains integers between 1 and 10 in descending order. 
- Test case `test_find_closest_elements()` verifies that the function selects the largest and second-largest elements when the list contains integers between 10 and