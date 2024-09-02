
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
    if k == len(arr):
        return sum(arr)

    total = 0
    k_th_element_two_digits = False

    for elem in arr[:k]:
        if elem < 10:
            total += elem
        elif elem < 100:
            if not k_th_element_two_digits:
                k_th_element_two_digits = True
                total += elem
            else:
                total -= elem

    return total

