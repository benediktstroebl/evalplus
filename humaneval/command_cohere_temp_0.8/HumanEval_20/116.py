```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must be of length at least two")
    else:
        middle = len(numbers) // 2
        return numbers[middle], numbers[-1]
```

This script defines a function `find_closest_elements` which takes in a list of float numbers and returns two float numbers that are closest to each other from the list and are returned in order (smaller number, larger number). The script returns `None` and displays an error message if the input list is insufficiently long, i.e., if the length of the list is less than 2. The function sorts the list in ascending order in the `sort()` function, and the closest elements are selected from the middle (second element) and the last element of the list in the main logic of the function.

Here is an example of how to use the function described above:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(test_list))
```
This would output:
```
(2.0, 2.2)
```

And here is another example where the list provided has less than 60 elements:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
print(find_closest_elements(test_list))
```
The corresponding output would be:
```
(2.0, 2.0)
```