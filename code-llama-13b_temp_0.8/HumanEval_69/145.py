
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
    # 1st solution
    # O(n^2) time | O(1) space
    # max = 0
    # for num in lst:
    #     if num > 0:
    #         times = lst.count(num)
    #         if num > max and times >= num:
    #             max = num
    # return max

    # 2nd solution
    # O(n) time | O(1) space
    count = {}
    max = 0
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        if num > max and count[num] >= num:
            max = num
    return max
