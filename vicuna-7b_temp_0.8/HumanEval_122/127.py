
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
    # Using a hashmap to store the two-digit numbers
    two_digit_map = {}
    for i in range(10):
        two_digit_map[str(i)] = i
    for i in range(k):
        # Looping through the first k elements of arr
        for j in range(len(arr)):
            if len(str(arr[j])) <= 2:
                # If the length of the str(arr[j]) is <= 2, append it to the two_digit_map
                if str(arr[j]) not in two_digit_map:
                    two_digit_map[str(arr[j])] = arr[j]
                    # If this is the first time seeing a number, adding it to the sum
                    if j == 0:
                        s = 0
                        for key in two_digit_map.keys():
                            s += two_digit_map[key]
                        return s
                else:
                    # If the number has already been seen, adding it to the sum
                    s = 0
                    for key in two_digit_map.keys():
                        s += two_digit_map[key]
                    s += arr[j]
                    # Updating the sum if this is the first time seeing the number
                    if j == 0:
                        s = 0
                        for key in two_digit_map.keys():
                            s += two_digit_map[key]
                        return s
    return 0
