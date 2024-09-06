```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    sorted_l = sorted(l)
    # Find the middle index
    middle_index = len(sorted_l) // 2
    if len(sorted_l) % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle elements
        median_value = (sorted_l[middle_index - 1] + sorted_l[middle_index]) / 2
    else:
        # Otherwise, return the middle element
        median_value = sorted_l[middle_index]
    return median_value
``` 

This function handles cases of even and odd-length lists, returning the average of the two middle numbers for even-length lists and the single middle number for odd-length lists. This should align with the test cases provided, but if the tests have specific additional cases, further adjustments may be needed. Let me know if you'd like me to cover any more scenarios or provide further code improvements.