
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    res_list = []
    lst.sort()
    for lst_item in lst:
        if lst_item[0] == 'a' or lst_item[0] == 'b' or lst_item[0] == 'c' or lst_item[0] == 'd' or lst_item[0] == 'e':
            lst_item = lst_item[1:]
        if len(lst_item) % 2!= 0:
            lst_item = lst_item[1:]
        res_list.append(lst_item)
    res_list.sort()
    return res_
