
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

    # Step 1: if no elements in arr that have less than 3 digits, return 0
    if not any(len(str(val)) < 3 for val in arr[:k]):
        return 0

    # Step 2: initialize sum and mod
    sum = 0
    mod = 10

    # Step 3: iterate through kth element
    for i in range(k):
        if len(str(arr[i])) < 3:
            # Step 4: add arr[i] to sum
            sum += arr[i]
            # Step 5: update mod to 100 if it is 10
            mod = 100 if mod == 10 else mod
        # Step 6: mod arr[i] with mod, update sum with sum of modded arr[i]
        else:
            sum += ((mod * arr[i]) // mod)
            # Step 7: update mod to 1000 if it is 100
            mod = 1000 if mod == 100 else
