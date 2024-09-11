Here's a Python script that solves the problem:
```markdown
### Median Calculator

This script calculates the median of a given list of numbers.

#### Code

```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    """
    return statistics.median(l)

# Test cases
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

#### Explanation

We use the built-in `statistics.median()` function to calculate the median. This function takes a list of numbers as input and returns the median as a float.

Note that this implementation assumes that the input list contains at least one element. If the list is empty, it will raise a `StatisticsError`.

If you want to implement the median calculation manually without using the `statistics` module, here's an alternative implementation:

```python
def median(l: list):
    """Return median of elements in the list l.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 0:
        # If the length of the list is even, the median is the average of the two middle numbers
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the length of the list is odd, the median is the middle number
        median = sorted_l[n // 2]
    
    return median
```