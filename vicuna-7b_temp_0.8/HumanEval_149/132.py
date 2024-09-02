
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
    n = len(lst)
    if n == 0:
        return []
    i = 0
    j = n-1
    while i < j:
        while i < j and lst[i].isalpha() and lst[i].isdigit():
            i = i + 1
        while i <= j and lst[j].isalpha() and lst[j].isdigit():
            j = j - 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i = i + 1
            j = j - 1
    return lst[i:j+1]
