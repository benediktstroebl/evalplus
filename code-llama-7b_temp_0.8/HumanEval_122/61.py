
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
    if len(arr) <= k:
        return sum(arr)

    # It's possible to do it in O(n) by using the built-in
    # python features, but the resulting solution is not
    # efficient enough as it has a linear time complexity.
    #
    # In the worst case scenario, we have to visit all the
    # elements of the input array and perform some operations
    # on each element.
    #
    # This is not good as we do not want to make use of the
    # already sorted elements of the input array.
    #
    # Also, if we have to perform some operation on each element,
    # it's not efficient as we have to use some other data
    # structure to store the already processed elements.
    #
    # So, we have to make use of the already sorted nature of
    # the input array.

    # After sorting the input array in ascending order, the first
    # k elements of the array will have at most two digits.

    # We can use the sortedness of the input array and slice the
    # first k elements to get our desired result.

    arr.sort()

    return sum(arr[:k])

