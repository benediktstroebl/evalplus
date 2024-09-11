Here's a Python script that implements the `median` function:

```markdown
### Median Calculation

This script defines a function `median` that calculates the median of a list of numbers.

#### Code

```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the numbers in the list.
    
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(l)

# Example usage
numbers = [3, 1, 2, 4, 5]
print("Median of:", numbers, "is", median(numbers))

numbers = [-10, 4, 6, 1000, 10, 20]
print("Median of:", numbers, "is", median(numbers))
```

#### Explanation

The `median` function uses the built-in `statistics.median` function from the Python standard library to calculate the median of the input list. This makes the code concise and efficient.

The example usage shows how to use the `median` function with two different lists of numbers.