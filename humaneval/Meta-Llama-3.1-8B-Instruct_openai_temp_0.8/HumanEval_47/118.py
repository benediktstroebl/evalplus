```python
import statistics
import math

def median(l: list):
    """Return median of elements in the list l."""
    
    # Check if the list is empty
    if len(l) == 0:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Calculate the length of the input list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, return the mean of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Test cases
def main():
    print("Median of [3, 1, 2, 4, 5] is:", median([3, 1, 2, 4, 5]))
    print("Median of [-10, 4, 6, 1000, 10, 20] is:", median([-10, 4, 6, 1000, 10, 20]))


if __name__ == "__main__":
    main()
```

Note that there's also a built-in function in Python to calculate the median, which you could use instead:

```python
import statistics

def median(l: list):
    """Return median of elements in the list l."""
    return statistics.median(l)
```

However, the above implementation does not use this built-in function, instead implementing the logic manually.