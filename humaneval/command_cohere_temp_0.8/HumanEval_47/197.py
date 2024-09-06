```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    sorted_list = sorted(l)
    # Finds the middle index
    middle_index = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle elements
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        # Otherwise, return the middle element
        median = sorted_list[middle_index]
    return median
``` 

This function handles cases of an empty list and returns the median based on the logic of handling even and odd-length lists. You can use this function to calculate the median of any list by passing it as an argument, like so:
```python
print(median([1, 2, 3, 4, 5]))  # Output: 3
``` 
This should return the median value of 3, as that value represents the middle value of the list [1, 2, 3, 4, 5].