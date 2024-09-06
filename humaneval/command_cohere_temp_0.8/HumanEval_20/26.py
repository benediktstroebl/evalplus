```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        diff = numbers[-1] - numbers[0]
        if diff < 0:
            # Swap the first and last numbers
            numbers[0], numbers[-1] = numbers[-1], numbers[0]
        return numbers[0], numbers[-1]
```

Here is a brief explanation of the code:
1. The function `find_closest_elements` takes a list of float numbers as input.
2. The input list is sorted, ensuring that the closest pair is always the first two elements.
3. If the list has less than two elements, an `IndexError` is raised, requiring at least two elements to function correctly.
4. The difference between the first and last numbers is computed, and if negative (indicating the closest pair is not in correct order), the numbers are swapped.
5. Finally, the first and last numbers are returned, being the closest pair. 

The function is designed to efficiently find the closest pair of numbers in a list, ensuring the correctness of the result through the use of sorting and indexing techniques.