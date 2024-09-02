
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
    def total_count(lst):
        lst_count = 0
        for ele in lst:
            lst_count += len(ele)
        return lst_count
        
    lst1_count = total_count(lst1)
    lst2_count = total_count(lst2)
    if lst1_count < lst2_count:
        return lst1
    elif lst1_count > lst2_count:
        return lst2
    else:
        return lst1
