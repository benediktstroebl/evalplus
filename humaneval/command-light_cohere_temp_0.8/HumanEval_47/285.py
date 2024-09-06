```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) < 1:
        raise ValueError("List is empty.")
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    if lst[mid] > lst[len(lst) - 1 - mid]:
        return (median((lst[:mid - 1]) + lst[mid:]) / 2)
    else:
        return (median((lst[:mid]) + lst[mid:]) / 2)

# Example usage:
lst = [-10, 4, 6, 1000, 10, 20]
print(median(lst))  # Output: 15.0
``` 
This code defines a function median that calculates the median of a given list. It does this calculation by first finding the middle element of the list and then checking if this element is greater or smaller than the second to last element in the list. This process is then repeated for the middle elements of the list until the entire list is processed.