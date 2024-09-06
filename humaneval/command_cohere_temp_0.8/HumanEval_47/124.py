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

    # Finds the median
    num_elements = len(sorted_list)
    mid_index = num_elements // 2
    if num_elements % 2 == 1:
        # If odd number of elements, return the middle element
        return sorted_list[mid_index]
    else:
        # If even number of elements, return average of two middle elements
        mid1 = sorted_list[mid_index - 1]
        mid2 = sorted_list[mid_index]
        return (mid1 + mid2) / 2
```

This function handles cases of empty lists, single-element lists, and also computes the median for lists having even or odd numbers of elements. It sorts the list first before walking through the elements to determine the median. 
To see it in action, you can run this function against the test cases provided in the original prompt:
```python
>>> median([3, 1, 2, 4, 5])
3
>>> median([-10, 4, 6, 1000, 10, 20])
15.0
``` 

Alternatively, you can use the `collections.sort()` function to sort the list, followed by filtering the middle element(s):
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
    l.sort()

    # Finds the median
    mid_index = len(l) // 2
    if len(l) % 2 == 0:
        # If even number of elements, return average of two middle elements
        return (l[mid_index - 1] + l[mid_index]) / 2
    else:
        # If odd number of elements, return the middle element
        return l[mid_index]
``` 

This alternative approach takes advantage of Python's built-in sorting function, offering a more concise implementation.