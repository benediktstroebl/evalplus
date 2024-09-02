
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
    # check length of all strings in the list
    min_len = max(len(s) for s in lst)

    # list to store all strings that have odd lengths
    odd_strs = []

    # loop through the list and check if all strings are of same length
    for s in lst:
        if len(s) != min_len:
            odd_strs.append(s)

    # sort the list by length of each word
    sorted_lst = sorted(lst, key=lambda x: x.length)

    # delete the odd_strs from the sorted list
    return [x for x in sorted_lst if x not in odd_strs]