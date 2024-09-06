
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
    lst_len = []
    lst_result = []

    # find the length of each item in list and append it into lst_len
    for i in range(len(lst)):
        lst_len.append(len(lst[i]))

    # sort the list based on its length, but preserve the order of the same length
    lst_len.sort(reverse=True)

    # create a dictionary that stores the index of each list item
    lst_index = dict(zip(lst, range(len(lst))))

    # sort the list based on the index
    lst_index_sorted = sorted(lst_index.items(), key=lambda x: x[1])

    # convert lst_index_sorted into a list, and append each item into lst_result
    for i in range(len(lst_index_sorted)):
        lst_result.append(lst_index_sorted[i][0])

    return lst_result
