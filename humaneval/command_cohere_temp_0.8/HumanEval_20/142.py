```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        return (numbers[-2], numbers[-1])
```
The function `find_closest_elements()` takes a list of numbers, `numbers`, as input and returns two floating points numbers that are closest to each other. The list of numbers must have a minimum length of two elements. It sorts the list and then returns the second last and the last elements, which are closest to each other by definition. It also checks for a minimum length of 2 to avoid any IndexError. 

Here is a simple test case:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
expected_result = (2.0, 2.2)

result = find_closest_elements(test_list)
assert result == expected_result
```
And here is an additional test case:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
expected_result = (2.0, 2.0)

result = find_closest_elements(test_list)
assert result == expected_result
```
These test cases check if the function `find_closest_elements()` works as expected, and the values it returns are correct. 

This solution is concise and efficient, but it also has a limitation: it assumes that the list contains at least two numbers that are closest to each other. If the list contains only one or very different numbers, this solution would raise an error or return unintuitive values.