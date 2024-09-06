
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    # The number of characters in the array
    n = len(arr)

    # The length of a palindrome
    # is always an odd number
    palindrome_length = n if n % 2 == 0 else n // 2

    # We can use a sliding window to count the number
    # of characters that are different, as shown below:
    #
    #   a b c d
    #
    #   0 0 1 2
    #
    #   a b b d
    #
    #   0 0 1 1
    #
    #   a a b d
    #
    #   0 0 0 1
    #
    #   a a b b
    #
    #   0 0 0 0
    #
    #   a a b c b a a
    #
    #   0 0 0 0 0 0 0
    #
    #   a a b c c b a a
    #
    #   0 0 0 0 0 0 0

    result = 0

    for i in range(n):
        # In the first iteration
        # we'll start by counting from the left side
        # and at the end of the for loop
        # we'll count from the right side
        # this will help us count the number
        # of characters that are different
        # in the first and last parts of the array
        # for example:
        #   1 2 3 4 5 6 7 8 9 10
        #   0 1 2 3 4 5 6 7 8 9
        #   0 0 1 2 3 4 5 6 7 8
        #   0 0 0 1 2 3 4 5 6 7
        #   0 0 0 0 1 2 3 4 5 6
        #   0 0 0 0 0 1 2 3 4 5
        #   0 0 0 0 0 0 1 2 3 
