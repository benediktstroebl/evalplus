```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize variables to compare each element against all others.
    closest_numbers = numbers[:]
    min_distance = float("inf")
    closest = [None] * len(numbers)

    # Compare each element against all others.
    for i in range(len(numbers)):
        other = closest_numbers[i] if closest[i] is None else closest[i]
        distance = numbers[i] - other
        closest[i] = (other, distance)
        min_distance = min(distance, min_distance)

    # Return the smallest and largest numbers.
    return closest[reversed()  # return the first two elements of the tuple

    # Example usage:
    numbers = [1.0, 2.0, 3.0, 4, 5.0, 2]
    - This script above, the find_closest_elements function takes a list of numbers and returns a tuple of the two closest numbers. The example usage demonstrates how to call the function with a list of numbers and prints the result.

Please note that this script assumes that the input list of numbers has at least two elements.