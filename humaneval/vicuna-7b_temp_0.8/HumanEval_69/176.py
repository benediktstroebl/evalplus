
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
    max_val = -1
    max_frequency = -1
    for num in lst:
        if num > 0 and num in [x[0] for x in lst if x[0] > num]:
            max_val = num
            max_frequency = lst.count(num)
            break
    return max_val, max_frequency

lst = [
[1, 2],
[2, 2],
[3, 1],
[4, 4],
[5, 4],
[4, 4],
[4, 4],
[4, 4],
[3, 3],
[2, 2],
[2, 2],
[1, 1],
[1, 1],
[1, 1]
]
max_val, max_frequency = search(lst)
