
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
    # set the smallest number to 1
    # start looping from the smallest to the largest
    # count the number of appearances
    # if the number of appearances is greater than or equal to the current number
    # return the current number
    # return -1 if no number was found
    # your code here
    min_n = min(lst)
    for n in range(min_n, max(lst) + 1):
        if lst.count(n) >= n:
            return n
    return -1

