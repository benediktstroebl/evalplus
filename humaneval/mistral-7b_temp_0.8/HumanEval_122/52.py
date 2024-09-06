
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
    # we could use a for loop to iterate through the first k elements
    # of the array and sum those elements, but that would not be optimal
    # because it would take O(n) time and O(1) space. Instead, we can
    # use the O(n) time and O(n) space solution of sorting the array in
    # ascending order, then iterating through the first k elements. This
    # is the O(n log n) time and O(n) space solution.
    # We could also use a binary search to find the first k elements,
    # but that would be O(n log k) time and O(1) space.

    # We could use a priority queue to store the elements that have
    # at most two digits, and then we can just pop the top two elements
    # and return their sum. This is the O(n log n) time and O(1) space
    # solution.

    # We could also use a heap to store the elements that have at most
    # two digits, and then we can just pop the top two elements and return
