
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
    ## Base condition -- if k is zero, return 0
    if k == 0:
        return 0

    ## Compute the sum of the elements of the array
    ## while keeping track of the number of digits in each
    ## element
    num_digits = 0
    sum_elements = 0
    for element in arr:
        num_digits += len(str(element))
        sum_elements += element

    ## If the sum of elements is less than the number of digits,
    ## we can simply return the sum
    if sum_elements <= num_digits:
        return sum_elements

    ## Otherwise, we will compute the number of elements that can be
    ## included in the sum without going over the limit of two digits
    k_within_limit = k
    while num_digits > k_within_limit * 2 and k_within_limit > 0:
        num_digits -= len(str(arr[k_within_limit - 1]))
        k_within_limit -= 1

    ## Iterate over the array until the limit has been reached
    ## and add each element to the sum
    total = 0
    for i in range(k_within_limit):
        total += arr[i]

    return total

