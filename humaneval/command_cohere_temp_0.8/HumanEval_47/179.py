```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None

    # Check if the list has only one element
    if len(l) == 1:
        return l[0]

    # Sort the list
    sorted_list = sorted(l)

    # Find the median
    length = len(sorted_list)
    middle_index = length // 2
    if length % 2 == 0:
        # If the number of elements is even, return the average of the two middle elements
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        # Otherwise, return the middle element
        median = sorted_list[middle_index]
    return median
``` 

This function handles cases of empty lists, single-element lists, and returns the median based on the number of elements in the list. Let's test it:
```python
test_list = [3, 1, 2, 4, 5]
print(median(test_list))  # Should print 3

test_list2 = [-10, 4, 6, 1000, 10, 20]
print(median(test_list2))  # Should print 15.0
``` 
This function should accurately compute the median of the given lists.