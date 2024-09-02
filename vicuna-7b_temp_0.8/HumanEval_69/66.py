
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
    count = [0] * 26 # Initialize the count array, each element represents the count of a unique element in the list
    for i in lst:
        count[lst[i]-'a'] += 1
    max_index = 0
    max_value = 0
    for i, val in enumerate(lst):
        if val > 0 and count[val-'a'] >= count[str(val)]:
            max_value = max(max_value, val)
            max_index = i
    return max_index