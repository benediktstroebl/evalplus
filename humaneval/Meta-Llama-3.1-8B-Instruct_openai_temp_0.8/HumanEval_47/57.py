Here is a Python script that solves the problem:
```markdown
## Median of a List

This script calculates the median of a list of numbers.

### Code

```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers

    Returns:
        float: The median of the list

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(l)
```

### Explanation

This script uses the `statistics` module, which is part of the Python Standard Library. The `median` function from this module calculates the median of a list of numbers.

### Usage

You can use this script like this:

```python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

Note that this script assumes that the input list is non-empty. If the input list is empty, it will raise a `StatisticsError`. If you want to handle this case, you can add a simple check at the beginning of the `median` function:

```python
def median(l: list):
    if not l:
        raise ValueError("cannot calculate median of empty list")
    return statistics.median(l)
```