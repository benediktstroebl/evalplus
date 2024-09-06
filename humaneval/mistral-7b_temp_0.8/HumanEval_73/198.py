
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
    # The most basic approach is to iterate through the array, comparing each element with its
    # corresponding element on the other side of the array. If the elements are not the same, we
    # can count the number of elements that need to be changed.

    # Time complexity: O(n^2)
    # Space complexity: O(1)

    # The time complexity can be improved by using a hash table to store the frequency of each element.
    # We can iterate through the array once and count the frequency of each element. Then, we can
    # iterate through the array again and change the elements that are not the same as the corresponding
    # element on the other side of the array. The time complexity will be O(n) because we only need to iterate
    # through the array twice. The space complexity will also be O(n) because we need to store the frequency of
    # each element in the hash table.

    # Another approach is to use a stack to store the elements of the array. We can iterate through the array
    # and push each element onto the stack. Then, we can pop the top two elements
