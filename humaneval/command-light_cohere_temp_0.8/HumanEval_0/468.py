```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return True if there is any two numbers in the list that are less than the given threshold, otherwise False.

    # Sort the numbers in ascending order.
    sorted_numbers = sorted(numbers)
    seen_pairs = []
    for i in range(len(sorted_numbers) - 1):
        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[i] - sorted_numbers[j] <= threshold:
                seen_pairs.append((sorted_numbers[i], sorted_numbers[j]))

    return seen_pairs is not empty
```

The above code defines a function called `has_close_elements` that takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the threshold. The function first sorts the, and then, iterates over the sorted list of numbers to find pairs of adjacent numbers. It checks if the each number in the pair is less than the threshold, and if so, it adds the pair to the seen_pairs list.