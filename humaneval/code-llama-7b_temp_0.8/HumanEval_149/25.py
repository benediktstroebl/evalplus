
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
    if len(lst) == 0:
        return lst
    else:
        temp_lst = sorted(lst, key=len)
        sorted_list = sorted(temp_lst, key=lambda x: len(x), reverse=True)
        result_list = []
        for i in range(0, len(sorted_list)):
            if len(sorted_list[i]) % 2 == 0:
                result_list.append(sorted_list[i])
        return result_list

    # return sorted(lst, key=lambda x: len(x))

