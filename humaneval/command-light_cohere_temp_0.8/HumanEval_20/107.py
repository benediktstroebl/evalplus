```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Calculate the distance between the first and last element in the list
    first, last = numbers[0] - numbers[-1]
    middle = (numbers[1] - first) + (last - numbers[0])
    # Find the smaller distance
    if middle < first - last:
        return first, last
    elif middle > first - last:
        return last, first
    else:
        # Find the closest element
        for i in range(len(numbers) - 1):
            current, next = numbers[i] - numbers[i + 1]
            if current < next:
                middle = current
                first = numbers[i]
                last = numbers[i + 1]
                break
        return first, last
```
The function takes a list of numbers as input and returns a tuple of the two closest elements in the list. It calculates the distance between the the first and last elements, then finds the smaller distance. The function then uses a inner loop to find the closer element, then updates the first and last variables. It repeats this until it distance becomes smaller than the current value. The function then returns the first and last element.