
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
    lst1_len = len(lst1)
    lst2_len = len(lst2)
    if lst1_len == lst2_len:
        return lst1
    elif lst1_len < lst2_len:
        lst1_len, lst2_len = lst2_len, lst1_len
        first_lst, second_lst = lst1, lst2
        first_lst, second_lst = second_lst, first_lst
    for i in range(lst1_len):
        if len(first_lst) == 0:
            return second_lst
        elif len(second_lst) == 0:
            return first_lst
        elif second_lst[0] == first_lst[0]:
            index = 0
            while index < lst1_len and index < len(second_lst):
                if len(first_lst) == 0:
                    return second_lst
                elif len(second_lst) == 0:
                    return first_lst
                elif second_lst[index] != first_lst[index]:
                    return first_lst
                index += 1
            second_lst.pop(0)
            first_lst.pop(0)
        else:
            if second_lst[0] < first_lst[0]:
                second_lst.pop(0)
            else:
                first_lst.pop(0)
    return first_lst


