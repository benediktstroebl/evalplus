
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
    def total_chars(lst):
        return sum(len(word) for word in lst)
    
    list1_total_chars = total_chars(lst1)
    list2_total_chars = total_chars(lst2)
    
    if list1_total_chars == list2_total_chars:
        return lst1
    elif list1_total_chars < list2_total_chars:
        return lst1
    return lst2

