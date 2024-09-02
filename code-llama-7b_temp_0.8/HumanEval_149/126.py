
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

    # method 1 - using set
    # return sorted(set(lst), key=lambda x: (len(x), x))

    # method 2 - without set
    return sorted(lst, key=lambda x: (len(x), x))

    # # method 3 - using lambda functions
    # return sorted(lst, key=lambda x: (len(x), x))

    # method 4 - using lambda functions
    # return sorted(lst, key=lambda x: (len(x), x), reverse=True)

    # method 5 - using lambda functions
    # return sorted(lst, key=lambda x: (len(x), x), reverse=False)

    # method 6 - using lambda functions
    # return sorted(lst, key=lambda x: (len(x), x), reverse=True)

    # method 7 - using lambda functions
    # return sorted(lst, key=lambda x: (len(x), x), reverse=False)




