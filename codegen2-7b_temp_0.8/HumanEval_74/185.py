
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
    def counting_chars(str1, str2):
        count = 0
        for x in str1:
            if x in str2:
                count += 1
        return count
    return lst1 if (counting_chars(lst1, lst2) == 0) else lst2 if (counting_chars(lst2, lst1) == 0) else lst1 if (counting_chars(lst1, lst2) < counting_chars(lst2, lst1)) else lst2
