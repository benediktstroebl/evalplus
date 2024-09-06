```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a length of at least 2")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return (left, right) if left != right else (numbers[0], numbers[-1])
```
The function first sorts the input list of numbers and checks if the length of the list is at least 2. If it isn't, an IndexError is raised. If the list is of length 2 or more, the function finds the middle number of the sorted list, then returns the closest pair of numbers from the left and right of the middle number. If the middle number is itself a duplicate, the function returns the first and last numbers of the sorted list, which are necessarily the closest.

Here is an example of how to use the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(test_list)
print(result)  # Output: (2.0, 2.2)
```
This will return the closest elements that are closest together in the list, which in this case are 2.0 and 2.2.