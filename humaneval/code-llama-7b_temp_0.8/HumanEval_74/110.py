
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
    # create a function to return number of characters in list items
    def count_chars(lst):
        chars_count = 0
        for item in lst:
            chars_count += len(item)
        return chars_count
    # create a list to append each list item that has less chars
    res = []
    lst1_chars = count_chars(lst1)
    lst2_chars = count_chars(lst2)
    if lst1_chars == lst2_chars:
        return lst1
    elif lst1_chars < lst2_chars:
        for i in range(len(lst1)):
            lst_item = lst1[i]
            lst_item_char = len(lst_item)
            if lst_item_char < lst2_chars:
                res.append(lst1[i])
        return res
    else:
        for i in range(len(lst2)):
            lst_item = lst2[i]
            lst_item_char = len(lst_item)
            if lst_item_char < lst1_chars:
                res.append(lst2[i])
        return res
