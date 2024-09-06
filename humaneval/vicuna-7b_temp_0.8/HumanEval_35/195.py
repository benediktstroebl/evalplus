

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Binary search is the most efficient way to find the maximum element in a sorted list
    low = 0
    high = len(l) - 1
    while low <= high:
        # Find the middle index where the left half of the list falls between the middle index and the right half
        mid = (low + high) // 2
        
        # Check if the middle element is the maximum element
        if l[mid] <= l[high]:
            return l[mid]
        else:
            # If the middle element is not the maximum element, move the left and right pointers
            low = mid + 1
        else:
            high = mid - 1
    # If the list is empty or not sorted, the maximum element is not in the list
    return l[0] if l else None