
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    arr = sorted(arr)
    # sort the array so we can use binary search
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            # if the current element is greater than the previous element, we know that the next element must be in sorted order
            # because the current element is the first of its group
            # so we can use this as a pivot and partition the array
            pivot = arr[i]
            start = i
            j = i
            while j < len(arr) and arr[j] <= pivot:
                arr[start:j+1] = arr[start:j] + [arr[j]]
                start = j
                j += 1
            arr[start:] = arr[start:] + [pivot-1]
            return len(arr) - start
    return 0