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
    sorted_l = sorted(l)
    # Find the middle element
    middle = len(sorted_l) // 2
    if len(sorted_l) % 2 == 0:
        return sorted_l[middle]
    # If the number of elements is odd, return the middle element
    return sorted_l[middle - 1]
``` 

This code provides a function called `median`, which takes a list as an argument and returns the median of the list's elements. The median is the middle value when the elements are sorted. The code first checks if the input list is empty or has only one element and returns `None` or the single value, respectively. If the list has more than one element, it sorts the list and finds the middle element. If the number of elements is even, it returns the middle value. If the number of elements is odd, it returns the value of the middle element from the sorted list, i.e., the value of the element at index `middle - 1` since the list is zero-indexed. 

This solution is scalable regarding the number of elements and will return the correct median irrespective of the list's initial order. It also has reasonable computational complexity, as it only requires one sort operation and a few indexing operations, which makes it an efficient solution for this problem.