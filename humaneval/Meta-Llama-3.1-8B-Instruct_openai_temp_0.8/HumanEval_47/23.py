### Median Calculation Script
```python
import statistics
from typing import List

def median(l: List[float]) -> float:
    """
    Return the median of elements in the list l.

    Args:
    l (List[float]): A list of numbers.

    Returns:
    float: The median of the list.

    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Use the median function from the statistics module to calculate the median
    return statistics.median(l)


# Example usage:
if __name__ == "__main__":
    numbers = [3, 1, 2, 4, 5]
    print(f"Median of {numbers}: {median(numbers)}")

    numbers = [-10, 4, 6, 1000, 10, 20]
    print(f"Median of {numbers}: {median(numbers)}")
```

### Notes

- This script utilizes the built-in `statistics.median()` function in Python's standard library, which simplifies the process of calculating the median.
- The script follows PEP 8 for code style and formatting.
- The example usage demonstrates the function's behavior with two different input lists.