### Median Calculation Script
#### Overview
This script defines a function `median` that calculates the median of a list of numbers. It uses the built-in `sorted` function to sort the list and then determines whether the list has an odd or even number of elements to calculate the median accordingly.

#### Code
```markdown
def median(l: list):
    """Return median of elements in the list l."""
    sorted_l = sorted(l)
    n = len(sorted_l)

    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_l[n // 2]

    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Example usage
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

#### Explanation
- The `median` function takes a list `l` as input and sorts it in ascending order.
- It then determines whether the list has an odd or even number of elements using the modulo operator (`n % 2 == 1`).
- If the list has an odd number of elements, the median is the middle element (`sorted_l[n // 2]`).
- If the list has an even number of elements, the median is the average of the two middle elements (`(mid1 + mid2) / 2`).
- The function returns the calculated median.

#### Notes
- This script uses the `sorted` function to sort the list, which has a time complexity of O(n log n). This is acceptable for most use cases, but for very large lists, a more efficient sorting algorithm like quicksort or heapsort may be necessary.
- The script assumes that the input list contains numbers. If the list can contain non-numeric values, additional error handling may be necessary.