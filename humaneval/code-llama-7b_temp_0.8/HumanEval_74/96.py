
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
    def total_word_count(lst):
        cnt = 0
        for item in lst:
            cnt += len(item)
        return cnt
    
    if len(lst1) == 0 or len(lst2) == 0:
        return []
    
    if total_word_count(lst1) == total_word_count(lst2):
        return lst1
    elif total_word_count(lst1) > total_word_count(lst2):
        return lst2
    else:
        return lst1
