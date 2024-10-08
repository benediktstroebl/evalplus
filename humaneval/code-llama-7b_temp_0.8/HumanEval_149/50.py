
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
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if len(lst[0]) < len(lst[1]):
            return lst
        else:
            return lst[::-1]
    else:
        pivot = len(lst) // 2
        if len(lst[pivot]) < len(lst[0]):
            pivot = pivot + 1
        lst1 = lst[:pivot]
        lst2 = lst[pivot:]
        return sorted(lst1) + sorted(lst2)
