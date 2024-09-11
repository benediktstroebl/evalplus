## Median Calculator
### Python Script
```markdown
### Code
```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    Raises:
        ValueError: If the list is empty.
    """
    try:
        return statistics.median(l)
    except statistics.StatisticsError:
        raise ValueError("List must not be empty")

### Example Use Cases
if __name__ == "__main__":
    # Test the function with the given examples
    print(median([3, 1, 2, 4, 5]))  # Output: 3
    print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

### Explanation

This script uses Python's built-in `statistics` module to calculate the median of a list. The `median()` function takes a list of numbers and returns the median value.

If the list is empty, it raises a `ValueError` with a message indicating that the list must not be empty.

In the example use cases, we test the function with the given examples and print the results.