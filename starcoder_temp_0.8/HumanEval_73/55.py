
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

    def _is_palindrome(arr):
        return arr == arr[::-1]

    def _get_min(arr):
        if _is_palindrome(arr):
            return 0

        def _get_next_values(arr, val):
            for i, x in enumerate(arr):
                if x == val:
                    return (i, arr[i + 1])

            return None

        prev = arr[0]
        changes = 0
        while True:
            next_val = _get_next_values(arr, prev)
            if not next_val:
                return changes

            idx, val = next_val
            arr[idx] = arr[idx + 1]
            arr[idx + 1] = val
            changes += 1

    return min([_get_min(arr), _get_min(arr[::-1])])

