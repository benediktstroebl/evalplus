```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return (left, right) if left == right else (min(left, right), max(left, right))
```

The function `find_closest_elements()` takes a list of numbers, sorts them, and then checks the elements at the middle index (or the closest indices if the length is odd). It then returns the smallest and largest of these elements if they are the same, or the smallest and largest values among them if they are not the same. This works for lists with an odd or even number of elements and handles cases where the list is too small or the values are equal. 

Here's a simple test case to verify the functionality:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
expected_result = (2.0, 2.2)

result = find_closest_elements(test_list)

assert result == expected_result, f"Expected {expected_result}, but got {result}"
``` 
The function also handles an edge case where the list contains fewer than two elements, raising an `IndexError` to alert the user that the input list is not valid.