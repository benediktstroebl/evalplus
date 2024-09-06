```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        return ()
    else:
        numbers.sort(key='<')
        first, second = numbers[0], numbers[1]
        while len(numbers) > 2:
            if numbers[2] < first or numbers[2] > second:
                numbers.remove(numbers[2])
            else:
                first, second = numbers[1], numbers[2]
        return (first, second)
```

This code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest elements in the list. It handles cases where the import a list of numbers is less than two and handles the edge case when there are more than two elements to consider.

The function uses the `sorted` function to sort the list of numbers in ascending order and then selects the first and second elements from the sorted list. It then continues to select the next element from the sorted list until it finds the smaller element to the larger element, at which point it will stop iterating.