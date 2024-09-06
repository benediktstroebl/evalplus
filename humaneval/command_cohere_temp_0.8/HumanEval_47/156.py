```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    sorted_list = sorted(l)
    # Find the middle index
    middle_index = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle elements
        median_value = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        # Otherwise, return the middle element
        median_value = sorted_list[middle_index]
    return median_value
``` 

This function handles cases of even and odd-length lists, returning the average of the two middle numbers for even-length lists and the single middle number for odd-length lists. This should correctly return the median for any list of numbers. Feel free to test it with your own inputs! Let me know if you would like any more explanations or want to dive deeper into the topic of statistical measuring in code!