
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
    # print(lst)
    # print(list(set(lst)))
    def frequency(x):
        return lst.count(x)

    def highest(x):
        if frequency(x) >= x:
            return True
        else:
            return False

    lst1 = list(set(lst))
    # print(lst1)
    lst2 = [i for i in lst1 if highest(i) and i > 0]
    # print(lst2)
    return max(lst2) if lst2 else -1

