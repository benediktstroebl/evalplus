
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
    def get_total_chars(lst):
        chars = 0
        for s in lst:
            chars += len(s)
        return chars
    
    def get_list_of_smaller_chars(lst1, lst2):
        list_1 = get_total_chars(lst1)
        list_2 = get_total_chars(lst2)
        if list_1 == list_2:
            return lst1
        return lst1 if list_1 < list_2 else lst2
    
    return get_list_of_smaller_chars(lst1, lst2)

