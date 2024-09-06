
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
    # 1. Solve without using division or multiplication.
    # 2. Solve without using sort.
    # 3. Solve without using sets.
    # 4. Solve without using any sorting or hashing.

    # 1. Division and multiplication - O(n^2)
    #
    #    TC: O(n^2)
    #    SC: O(1)
    #
    #    for i in range(k):
    #        sum = 0
    #        for j in range(i, k):
    #            sum += arr[j]
    #        arr.append(sum)

    # 2. Sort - O(n log n)
    #
    #    TC: O(n log n)
    #    SC: O(n)
    arr = sorted(arr)

    # print(arr)

    sum = 0
    for i in range(k):
        sum += arr[i]

    # 3. Set - O(n)
    #
    #    TC: O(n)
    #    SC: O(n)
    #
    # set_ = set(arr[:k])
    #
    # for i in range(k, len(arr)):
    #     set_.add(arr[i])
    #
    # for i in set_:
    #     sum += i

    # 4. Hash - O(n)
    #
    #    TC: O(n)
    #    SC: O(n)
    #
    # hash_ = {}
    # for i in range(k):
    #     if arr[i] in hash_:
    #         hash_[arr[i]] += 1
    #     else:
    #         hash_[arr[i]] = 1
    #
    # for key, value in hash_.items():
    #     if value <= 2:
    #         sum += key

    return sum
