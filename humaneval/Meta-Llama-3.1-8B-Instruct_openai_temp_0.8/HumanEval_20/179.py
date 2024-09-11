### Find Closest Elements
#### Python Script

```markdown
from typing import List, Tuple
import itertools

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of floating point numbers with at least two elements.

    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in order.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Find the pair with the smallest difference
    closest_pair = min(pairs, key=lambda pair: abs(pair[0] - pair[1]))

    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers and returns a tuple of the two numbers that are closest to each other. The function uses the `itertools.combinations` function to generate all possible pairs of numbers, and then finds the pair with the smallest difference using the `min` function with a lambda function as the key. The script also includes some test cases to demonstrate the function's behavior.