### Calculating the Median of a List
#### Using the QuickSelect Algorithm

Here's a Python script that uses the QuickSelect algorithm to efficiently calculate the median of a list:

```markdown
### Code
```python
import random

def quickselect(arr, k):
    """
    Find the k-th smallest element in the list.

    Args:
    arr (list): The list of elements.
    k (int): The index of the desired element (0-indexed).

    Returns:
    int or float: The k-th smallest element in the list.
    """
    if len(arr) == 1:
        return arr[0]

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quickselect(right, k - len(left) - len(middle))


def median(lst):
    """
    Return the median of elements in the list.

    Args:
    lst (list): The list of elements.

    Returns:
    int or float: The median of the list.
    """
    n = len(lst)
    if n % 2 == 1:
        return quickselect(lst, n // 2)
    else:
        mid1 = quickselect(lst, n // 2 - 1)
        mid2 = quickselect(lst, n // 2)
        return (mid1 + mid2) / 2


# Example usage
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

#### Explanation
This script first defines a helper function `quickselect` that implements the QuickSelect algorithm to find the k-th smallest element in a list. The `median` function then uses `quickselect` to calculate the median of the list by calling `quickselect` with k = n/2 (or k = (n-1)/2 for even-length lists). If the list has an odd length, the median is simply the middle element. For even-length lists, the median is the average of the two middle elements.