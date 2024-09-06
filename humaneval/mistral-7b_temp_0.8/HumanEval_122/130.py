
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

    # Your code here
    new_list = []
    # take first k elements
    for i in range(k):
        new_list.append(arr[i])

    # get sum of the elements in the list with length 2 or less
    sum = 0
    for i in range(len(new_list)):
        if len(str(new_list[i])) <= 2:
            sum += new_list[i]

    return sum

