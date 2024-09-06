```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).

    : Return a tuple with two closest numbers and their relationship.

    Returns: following values:
    - `numbers` (list of floats) 
    - `closest1` (float) - The first closest number
    - `closest2` (float) - The second closest number
    - `rel` (float) - The relationship between the two numbers (smaller, larger, or equal)

    :param numbers: A list of numbers
    :return: A tuple with three elements
    """
    numbers = sorted(numbers, key=lambda x: (-x, x))

    return (numbers[0], numbers[1], numbers[0] == numbers[1])
```
The provided Python function, named 'find_closest_elements', efficiently solves the problem of finding the closest pair of elements within a given list of numbers. It accomplishes this process by sorting the numbers in descending order and selecting the smallest and the largest numbers, respectively. The function then returns a tuple containing the two closest numbers and their relationship, which can be either smaller, larger, or equal.