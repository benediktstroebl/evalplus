
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
    # Solution 1:
    return sorted([word for word in lst if len(word)%2==0], key=len)

    # Solution 2:
    # lst = sorted(lst, key=len)
    # for word in lst:
    #     if len(word)%2!=0:
    #         lst.remove(word)
    # return lst
    #
    #
    # Solution 3:
    # temp_lst = []
    # for word in lst:
    #     if len(word)%2==0:
    #         temp_lst.append(word)
    # temp_lst.sort()
    # return temp_lst
    #
    # Solution 4:
    # lst.sort(key=len)
    # for word in lst:
    #     if len(word)%2!=0:
    #         lst.remove(word)
    # lst.sort()
    # return lst
