
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

    def palindrome_permutation(arr):
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        num = 0
        for i in count:
            if count[i] % 2 == 1:
                num += 1
            if num > 1:
                return False
        return True
    
    def get_change(arr):
        change = 0
        for i in range(len(arr)):
            change += abs(arr[i] - (len(arr) + 1 - i))
        return change
    
    return get_change(arr) - get_change(sorted(arr))

