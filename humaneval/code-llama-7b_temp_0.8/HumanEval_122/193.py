
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
    # initialize a new list and append first k elements to it
    new_list = []
    for i in range(k):
        new_list.append(arr[i])

    # initialize sum
    sum = 0

    # iterate through new_list
    for i in range(len(new_list)):
        # extract the last digit of the element
        rem = new_list[i] % 10

        # if the last digit is smaller than or equal to 9, add that element to sum
        if rem <= 9:
            sum += new_list[i]

    return sum
