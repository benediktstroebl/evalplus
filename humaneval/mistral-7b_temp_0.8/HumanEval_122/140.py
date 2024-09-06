
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
    # TODO: return the sum of the elements with at most two digits from the first k elements of arr

    # 1. check the length of the arr
    if len(arr) < 2:
        return 0

    # 2. initialize sum to 0
    sum = 0

    # 3. iterate through the arr
    for i in range(k):
        # 4. check if the element has more than 2 digits
        if len(str(arr[i])) > 2:
            continue
        # 5. add the element to the sum
        sum += arr[i]

    return sum

