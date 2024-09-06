
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
    # sort the array
    arr = sorted(arr)

    # initialize the sum
    sum = 0

    # check if there are more than k elements
    if len(arr) > k:
        # initialize variables to check if the sum is good
        count = 0
        good = 0

        # iterate through the rest of the elements
        for i in range(k, len(arr)):
            # check if the current element is good
            if (arr[i] < sum + k) or (arr[i] >= sum + 10 * k):
                count += 1
                good += (arr[i] >= sum + 10 * k)
            else:
                count += 1
                good += (arr[i] >= sum)

        # check if the current element is good
        if count == 0:
            # if the current element is good, update the sum
            sum += arr[i]
            if sum >= 10 * k and sum >= 10 * k - k // 2:
                return sum

        # if the current element is not good, update the sum
        if good:
            sum += arr[i]
            if sum >= 10 * k and sum >= 10 * k - k // 2:
                return sum
    else:
        # there are less than k elements
        # use the remaining elements
        if sum + k <= 10 * k:
            return sum
        else:
            return 0
