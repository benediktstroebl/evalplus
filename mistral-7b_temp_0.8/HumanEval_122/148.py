
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
    nums = []
    for i in range(k):
        # add integers in first k elements to the list
        nums.append(arr[i])

    # filter out all integers in nums whose digits are more than 2
    # append the integers to a new list
    filtered = filter(lambda num: len(str(num)) > 2, nums)
    filtered = list(filtered)

    # find the sum of integers in filtered
    sum_of_integers = sum(filtered)
    return sum_of_integers

