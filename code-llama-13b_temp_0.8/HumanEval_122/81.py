
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
    # Time Complexity: O(k)
    # Space Complexity: O(1)
    # Note: count = k
    # counter = 0
    # count = 0
    # sum = 0
    # for i in arr:
    #     # Sum of first k elements
    #     if count < k:
    #         sum += i
    #         count += 1
    #     else:
    #         # If the next element's length is less than 2,
    #         # then replace the element with the next element
    #         if len(str(arr[counter])) < 2:
    #             # print(counter, arr[counter])
    #             sum -= arr[counter]
    #             sum += arr[counter + 1]
    #             # print(arr[counter], arr[counter + 1])
    #             counter += 1
    # return sum
    count = 0
    sum = 0
    for i in arr:
        # Sum of first k elements
        if count < k:
            sum += i
            count += 1
        else:
            # If the next element's length is less than 2,
            # then replace the element with the next element
            if len(str(arr[count])) < 2:
                # print(counter, arr[counter])
                sum -= arr[count]
                sum += arr[count + 1]
                # print(arr[counter], arr[counter + 1])
                count += 1
    return sum
