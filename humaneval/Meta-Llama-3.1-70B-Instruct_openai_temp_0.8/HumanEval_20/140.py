```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    :param numbers: A list of numbers
    :return: A tuple of the two closest numbers in ascending order
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = ()

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
print(find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0]))  # Expected output: (10.0, 20.0)
print(find_closest_elements([5.5, 1.1, 3.3, 4.4, 2.2]))  # Expected output: (2.2, 3.3)

try:
    find_closest_elements([1.0])
except ValueError as e:
    print(e)  # Expected output: The list must have at least two elements
```