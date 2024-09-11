```python
import statistics

def median(numbers: list) -> float:
    """Return median of elements in the list numbers."""
    return statistics.median(numbers)

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

However, if you want to implement the median calculation manually, here's how you can do it:

```python
def median(l: list) -> float:
    """Return median of elements in the list l."""
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 1:
        # If the length of the list is odd, the median is the middle element
        return sorted_l[n // 2]
    else:
        # If the length of the list is even, the median is the average of the two middle elements
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This manual implementation handles both odd and even length lists, ensuring accurate calculation of the median.