
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    arr.sort(reverse=True)
    for i in range(k):
        arr.append(0)
    first_half = arr[:k]
    second_half = arr[k:]
    first_half = first_half[::2]
    second_half = second_half[1:]
    second_half.append(0)
    sum_ = sum(first_half) + sum(second_half)
    return sum_
