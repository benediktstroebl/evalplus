
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
    # This is the new list with odd length deleted
    new_lst = []
    for i in range(0, len(lst), 2):
        odd_lst = lst[i]
        even_lst = lst[i + 1]
        new_lst.append(odd_lst[0])
        new_lst.append(even_lst[0])

    # This is the sorted list with even length deleted
    sorted_lst = sorted(new_lst)

    return sorted_lst
