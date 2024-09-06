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

    # Finds the median in the case of an even number of elements
    if len(sorted_list) % 2 == 0:
        return (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2

    # Finds the median in the case of an odd number of elements
    else:
        return sorted_list[len(sorted_list) // 2]
```

This function handles two main cases:
1. If the length of the list is 1, it simply returns the single element in the list.
2. If the list has more than one element, it sorts them and then checks if the length of the list is even. If it is, it takes the average of the two middle elements. If the length is odd, it simply returns the middle element. 

To better understand the function, here is an example usage of the function:
```python
print(median([1, 2, 3, 4, 5]))  # 3
print(median([2, 3, 4, 5, 7, 11, 31]))  # 5.0
``` 

This should return the median of the given list, conforming to the specified API.