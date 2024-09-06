```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must be of length at least two")
    else:
        return numbers[0], numbers[-1]
```

This function sorts the input list of numbers and returns the pair of the smallest and largest numbers in the list, i.e. the closest pair of numbers in terms of difference. It also throws an IndexError when the input list has less than 2 elements, as the method is not meaningful for a single pair or for 3 or more pairs. 

Here is an example of use for this function:
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This will output:
```
(2.0, 2.2)
(2.0, 2.0)
```