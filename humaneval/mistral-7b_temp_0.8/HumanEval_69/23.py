
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
    # Write your code here.
    # return -1 if no greater than 0 value appears in the list more than it's value
    # in the list
    # return the value if there is a greater than 0 value that appears in the list more than it's value in the list
    if len(lst)==0:
        return -1
    greatest_int = max(lst)
    frequency = lst.count(greatest_int)
    if frequency >= greatest_int:
        return greatest_int
    return -1

