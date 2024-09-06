
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

    def count_occurrences(lst, value):
        return lst.count(value)
    
    positive_numbers = [lst[i] for i in range(len(lst)) if lst[i] > 0]
    pos_count = []
    for i in positive_numbers:
        if count_occurrences(lst, i) >= i:
            pos_count.append(i)

    return max(pos_count) if pos_count else -1



