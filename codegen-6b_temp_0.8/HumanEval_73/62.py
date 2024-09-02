
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    def make_palindrome(arr, changes):
        # Given a set of changes, checks if the new array is palindromic
        arr = arr[:]  # Make a copy of the array
        for change in changes:
            arr[change] = (arr[change] + 1) % 2   # Modify each element

        return all(arr[i] == arr[i-1] for i in range(1, len(arr)))

    changes = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            changes.append((i, j))    # Add new possible changes

    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            changes.append((j, i))    # Add new possible changes

    return min([len(arr)-1 - j for i in range(0, len(arr)/2) for j in range(i+1, len(arr)-i) if make_palindrome(arr[i:j], changes)])

