
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
    # Check the condition
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst[0]
    # Creating a new list with unique elements
    uniq_lst = sorted(lst)
    # Removing the odd-length elements from the list
    unique_lst = [x for x in uniq_lst if len(x) % 2 != 0]
    # Combine the remaining elements in the list
    last_lst = [x for x in uniq_lst if len(x) % 2 == 0]
    # Returning the sorted list
    return unique_lst + last_lst
