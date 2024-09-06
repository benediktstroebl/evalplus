
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
    def total_char_lst(lst):
        return sum([len(i) for i in lst])
    t_chars_lst1 = total_char_lst(lst1)
    t_chars_lst2 = total_char_lst(lst2)
    if t_chars_lst1 < t_chars_lst2:
        return lst1
    elif t_chars_lst1 > t_chars_lst2:
        return lst2
    else:
        return lst1

