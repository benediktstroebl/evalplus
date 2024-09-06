
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''

    def helper(arr, i, target):
        if i == len(arr):
            return -1

        if arr[i] > 0 and arr[i] >= target:
            return arr[i]

        if arr[i] > 0:
            return -1

        return helper(arr, i+1, target)

    return helper(lst, 0, lst[0])

