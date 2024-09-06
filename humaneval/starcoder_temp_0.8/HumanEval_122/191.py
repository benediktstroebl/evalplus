
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
    assert len(arr) > 0 and k > 0 and k <= len(arr)
    # Approach 1 - 2 nested loops O(k*k)
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if abs(arr[i]-arr[j]) <= 9:
    #             return sum(arr[i:j])

    # Approach 2 - use a hashmap O(k)
    unique_nums = set()
    for i in range(k):
        unique_nums.add(arr[i])
    for j in range(k, len(arr)):
        if abs(arr[j-k]-arr[j]) <= 9:
            unique_nums.add(arr[j])
        else:
            unique_nums.remove(arr[j-k])
    return sum(unique_nums)


