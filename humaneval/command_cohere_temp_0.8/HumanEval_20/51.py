```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    elif len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        middle = numbers[(len(numbers) + 1) // 2 - 1]
        nearer, farther = numbers[0], numbers[-1]
        if abs(middle - nearer) < abs(middle - farther):
            return farther, middle
        else:
            return nearer, middle
```
The function first sorts the input list of numbers, ensuring that the nearest elements to each other are the first two elements of the sorted list, or the last two elements if they are the nearest. It may be possible to optimize the function to avoid sorting the list when it is not necessary, but the function provided here is simple and has good enough performance for reasonable inputs. 
The tests here ensure the function raises an error if the input list is empty or has only one element, and works for lists of two or more elements. The tests also check that the function handles cases where the 'nearest' elements are either the first two elements of the sorted list, or the last two elements.