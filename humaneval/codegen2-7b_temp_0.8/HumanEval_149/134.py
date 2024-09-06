
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
    if not lst:
        return []
    if len(lst) == 1:
        return lst
    lst = sorted(lst, key=len)
    start = 0
    end = len(lst) - 1
    while start < end:
        if len(lst[start]) % 2!= 0:
            start += 1
            continue
        if len(lst[end]) % 2!= 0:
            end -= 1
            continue
        else:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
    return lst
