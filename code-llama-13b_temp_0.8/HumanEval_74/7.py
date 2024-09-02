
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
    
    def get_sum(lst):
        sum_num = 0
        for string in lst:
            sum_num += len(string)
        return sum_num
    
    lst1_num = get_sum(lst1)
    lst2_num = get_sum(lst2)
    
    if lst1_num < lst2_num:
        return lst1
    if lst2_num < lst1_num:
        return lst2
    return lst1

