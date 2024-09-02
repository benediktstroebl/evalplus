
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
    #   for i in range(0, len(lst)):
    #       for j in range(0, len(lst)):
    #           if i != j and len(lst[i]) != len(lst[j]):
    #               if lst[i] not in lst:
    #                   lst.insert(j, lst[i])
    #                   lst.remove(lst[j])
    #               else:
    #                   lst.insert(j, lst[i])
    #                   lst.remove(lst[j])
    #   return lst

    #   for i in range(0, len(lst)):
    #       if len(lst[i]) % 2 == 0:
    #           lst.append(lst[i])
    #           lst.remove(lst[i])

    #   lst.sort()
    #   return lst

    # lst.sort()
    # print(lst)
    # lst_sorted = list()
    # for i in range(0, len(lst)):
    #     if len(lst[i]) % 2 == 0:
    #         lst_sorted.append(lst[i])
    # lst_sorted.sort()
    # return lst_sorted

    # print(lst)
    lst.sort(key=len)
    # lst.sort(key=len, reverse=True)
    return lst


