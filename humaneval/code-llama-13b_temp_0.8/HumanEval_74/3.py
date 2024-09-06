
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
    def count_total(lst):
        count = 0
        for i in lst:
            count += len(i)
        return count
    
    count_lst1 = count_total(lst1)
    count_lst2 = count_total(lst2)
    
    if count_lst1 < count_lst2:
        return lst1
    if count_lst1 > count_lst2:
        return lst2
    return lst1
    
    
