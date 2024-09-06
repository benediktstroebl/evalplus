
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    def sum_char(lst):
        num = 0
        for i in lst:
            num += len(i)
        return num
    
    def find_max(lst1, lst2):
        if len(lst1) > len(lst2):
            return lst1
        elif len(lst2) > len(lst1):
            return lst2
        else:
            return lst1
        
    if sum_char(lst1) < sum_char(lst2):
        return lst1
    elif sum_char(lst2) < sum_char(lst1):
        return lst2
    else:
        return find_max(lst1, lst2)

