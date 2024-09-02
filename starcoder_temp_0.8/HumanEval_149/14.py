
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
    if len(lst) <= 1:
        return lst
    half = len(lst)//2
    left = sorted_list_sum(lst[:half])
    right = sorted_list_sum(lst[half:])
    i = 0
    j = 0
    ret = []
    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            ret.append(left[i])
            i += 1
        elif len(right[j]) < len(left[i]):
            ret.append(right[j])
            j += 1
        elif left[i] == right[j]:
            ret.append(left[i])
            ret.append(right[j])
            i += 1
            j += 1
    while i < len(left):
        ret.append(left[i])
        i += 1
    while j < len(right):
        ret.append(right[j])
        j += 1
    return ret
