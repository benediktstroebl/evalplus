```markdown
### Calculate Median of a List
#### Python Solution

Here is a Python function that calculates the median of a list of numbers.

```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.

    Args:
    l (list): A list of numbers.

    Returns:
    float: The median of the list.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(l)

# Example usage:
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

### Note
This solution uses the built-in `statistics.median` function to calculate the median. This function is efficient, reliable, and concise.
```

Alternatively, if you want to implement the median calculation manually without using the `statistics` module, you can use the following code:

```markdown
### Calculate Median of a List
#### Manual Solution

Here is a Python function that calculates the median of a list of numbers.

```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
    l (list): A list of numbers.

    Returns:
    float: The median of the list.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 0:
        # If the list has an even number of elements, the median is the average of the two middle elements.
        median = (sorted_l[n//2 - 1] + sorted_l[n//2]) / 2
    else:
        # If the list has an odd number of elements, the median is the middle element.
        median = sorted_l[n//2]

    return median

# Example usage:
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```
```