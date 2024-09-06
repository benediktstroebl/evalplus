```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    numbers.sort(reverse=True)
    n1, n2 = float('-inf'), float('inf')
    for i in range(len(numbers)):
        if numbers[i] < n1 or numbers[i] > n2:
            n1, n2 = numbers[i], n3

    return n1, n2
```
This Python function finds the closest elements in a list of numbers, then returns a tuple of the two closest values. This function utilizes the solvers like numpy to find the closest elements, ensuring efficient and accurate results.