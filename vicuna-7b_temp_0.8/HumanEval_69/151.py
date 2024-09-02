
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
    n = len(lst)
    if n == 0:
        return -1
    elif n == 1:
        return lst[0]
    else:
        max_index = 0
        max_val = lst[0]
        for i in range(1, n):
            if lst[i] > max_val:
                max_index = i
                max_val = lst[i]
        return max_val

lst = [2, 2, 2, 3, 1, 4, 4, 4]
result = search(lst)
print(result)