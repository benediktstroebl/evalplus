### Median Calculation in Python

The following Python script defines a function `median` that calculates the median of a given list of numbers.

```markdown
### Code

```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the list elements.
    
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(l)

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(median(numbers))

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))
```

### Explanation

The `median` function uses the `statistics.median` function from Python's standard library, which calculates the median of a list of numbers. This approach is simpler and more efficient than implementing a custom median calculation algorithm.

### Advantages

*   No need to implement a custom median calculation algorithm, reducing the risk of errors and improving code readability.
*   Utilizes a well-tested and efficient function from the standard library.
*   Handles edge cases, such as empty lists or lists with duplicate elements.