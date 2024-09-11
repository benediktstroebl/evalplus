### Median Calculation Python Script
```markdown
### Problem Statement:
### 
### Define a function `median(l: list)` that returns the median of a given list `l`.
### The median is the middle value in a sorted list of numbers.
### If the list has an even number of elements, the median is the average of the two middle numbers.

### Solution:
```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the list.
    """
    # Use the median function from the statistics module to calculate the median
    return statistics.median(l)

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

### Explanation:
The `median` function takes a list of numbers as input and returns the median using the `statistics.median` function. This function handles both odd and even length lists correctly, returning the average of the two middle numbers for even length lists.

### Note:
This solution uses the `statistics.median` function from Python's standard library, which is more efficient and accurate than implementing a custom median calculation. If you need to implement the median calculation manually, you can use a similar approach to the following code:
```python
def median_manual(l: list):
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, return the middle element
    if n % 2 == 1:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
```
However, the `statistics.median` function is generally more efficient and accurate, and is recommended for use in most cases.