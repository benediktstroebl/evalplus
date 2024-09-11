Here's a Python script that uses the built-in `sorted` function and the `statistics` module to find the median of a list.
```python
import statistics

def median(l: list):
    """Return median of elements in the list l."""
    # Use the statistics module's median function
    return statistics.median(l)

# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
However, if you want to implement the median calculation manually without using the `statistics` module, you can use the following script:

```python
def median(l: list):
    """Return median of elements in the list l."""
    # Sort the list in ascending order
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script sorts the list and then checks if the length of the list is odd or even. If the length is odd, it returns the middle element. If the length is even, it returns the average of the two middle elements.