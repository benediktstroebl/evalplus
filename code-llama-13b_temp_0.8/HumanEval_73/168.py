
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
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    if arr == arr[::-1]:
        return 0

    def generate_permutations(arr):
        if len(arr) == 1:
            yield arr
            return
        for i in range(len(arr)):
            for perm in generate_permutations(arr[:i] + arr[i+1:]):
                yield [arr[i]] + perm

    min_len = len(arr)
    for perm in generate_permutations(arr):
        if perm == perm[::-1]:
            min_len = min(min_len, len(perm))
    return len(arr) - min_len
