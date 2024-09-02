

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    #write your code here
    # assuming it is sorted array
    # if it is not sorted you can convert it to sorted
    # use two pointers one starting from the end and one from the start
    # keep traversing until you find either the two numbers you need or
    # you reach the end of the array
    # if you reached the end and did not find anything return False
    # if you found two numbers that sum to zero return True
    # increment the smaller pointer and decrement the bigger one

    l = sorted(l)
    left, right = 0, len(l) - 1
    while left < right:
        sum = l[left] + l[right]
        if sum == 0:
            return True
        if sum < 0:
            left += 1
        else:
            right -= 1
    return False

