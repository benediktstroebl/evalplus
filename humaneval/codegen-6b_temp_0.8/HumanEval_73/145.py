
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
    if len(arr) == 1:
        return 0

    def is_palindrome(arr):
        return arr == arr[::-1]

    from heapq import heappop, heappush
    change_map = {
        x: y
        for x in arr
        for y in [x, - x]
    }

    heap = [-x for x in arr if x not in change_map]
    heapify(heap)
    min_changes_to_make_palindrome = len(arr)

    while heap:
        current = heappop(heap)
        current_changes = change_map[current]
        if is_palindrome(current_changes):
            return min_changes_to_make_palindrome - current_changes

        min_changes_to_make_palindrome -= current_changes

        for i in range(len(current_changes)):
            if current_changes[i] not in change_map:
                continue
            change_to = current_changes[i]
            heappush(heap, - change_to)

    return min_changes_to_make_palindrome

assert smallest_change([1,2,3,5,4,7,9,6]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([3,2,3,2,3]) == 2
assert smallest_change([3,3,1,2,2,3,2,1]) == 3
assert smallest_change([1,2,3,5,4,7,9,6]) == 4
assert smallest_change([1,2,3,5,4,7,9,6,4,3,2,1]) == 5
assert smallest_change([1,2,3,2,1]) == 0
assert smallest_change([1,2,3,5,4,3,2,2,1]) == 5
assert smallest_change([6,7,1,2,9,5,3,4]) == 4
assert smallest_change([6