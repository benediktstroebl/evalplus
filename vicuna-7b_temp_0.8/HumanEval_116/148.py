
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # Using 2 pointers to keep track of left and right of sorted array
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Find middle index where left and right pointers are equal
        mid = (left + right) // 2
        
        # If middle index has more ones than the left pointer,
        # swap middle element with the left pointer and increment left pointer
        if (arr[mid] < 0).bit_length() > (arr[left] < 0).bit_length():
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
        # If middle index has less ones than the right pointer,
        # swap middle element with the right pointer and decrement right pointer
        elif (arr[mid] < 0).bit_length() < (arr[right] < 0).bit_length():
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1

    return arr