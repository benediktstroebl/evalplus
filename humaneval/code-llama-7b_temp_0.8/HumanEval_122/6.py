
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
    # two pass algorithm
    # pass 1: get the sum of first k elements with at most two digits
    # pass 2: get the sum of first k elements with at most two digits
    # return the difference of the two sums
    arr.sort()

    count = 0
    total = 0
    for elem in arr[:k]:
        if elem < 100:
            total += elem
            count += 1

    # the sum of first k elements with at most two digits
    sum1 = total

    # print(f"sum1: {sum1}")

    count = 0
    total = 0
    for elem in arr[:k]:
        if elem < 100:
            total += elem
            count += 1
        else:
            total += elem % 10

    # the sum of first k elements with at most two digits
    sum2 = total

    # print(f"sum2: {sum2}")

    return sum1 - sum2

