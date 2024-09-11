```markdown
### Find Closest Elements in a List
#### Problem
Given a list of numbers, find and return two numbers that are the closest to each other.

#### Solution
```python
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: Two numbers that are the closest to each other.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Calculate the absolute difference of each pair
    differences = [(a, b, abs(a - b)) for a, b in pairs]

    # Find the pair with the smallest difference
    smallest_diff_pair = min(differences, key=lambda x: x[2])

    # Return the pair with the smallest difference
    return smallest_diff_pair[:2]
```

#### Example Use Cases
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```
This code uses the `itertools` module to generate all possible pairs of numbers, calculates the absolute difference of each pair, and then finds the pair with the smallest difference. The pair with the smallest difference is returned as a tuple.