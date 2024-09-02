
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
    lst_copy = lst.copy()
    lst_len = []
    for i in lst_copy:
        lst_len.append(len(i))
    lst_len.sort()
    lst_sorted = []
    for i in lst_len:
        for j in lst_copy:
            if len(j) == i:
                lst_sorted.append(j)
    lst_sorted.sort()
    return lst_sorted

