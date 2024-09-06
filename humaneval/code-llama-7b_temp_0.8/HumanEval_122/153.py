
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
    # for i in range(len(arr)):
    #     if len(str(arr[i])) <= k:
    #         print(arr[i])

    # arr.sort(reverse=True)
    # print(arr[k])

    # sum = 0
    # for i in range(k):
    #     sum += arr[i]
    #     print(sum)

    # sum = 0
    # for i in range(len(arr)):
    #     if i < k:
    #         sum += arr[i]
    #     else:
    #         if len(str(arr[i])) > len(str(arr[i - k])):
    #             sum -= arr[i - k]
    #         sum += arr[i]
    #     print(sum)

    # sum = 0
    # for i in range(len(arr)):
    #     if i < k:
    #         sum += arr[i]
    #     else:
    #         for j in range(i - k + 1, i):
    #             if len(str(arr[j])) > len(str(arr[i])):
    #                 sum -= arr[j]
    #         sum += arr[i]
    #     print(sum)

    sum = 0
    for i in range(k):
        sum += arr[i]
    print(sum)

    for i in range(k, len(arr)):
        sum += arr[i]
        if len(str(arr[i])) > len(str(arr[i - k])):
            sum -= arr[i - k]
        print(sum)


