
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
    # Start with a copy of the original list
    lst = [x for x in lst]

    # Remove all odd length strings
    while lst:
        if len(lst[0]) % 2 == 0:
            # If the length is even, keep the string
            lst.pop(0)
        else:
            # If the length is odd, skip the next iteration
            continue

    # Sort the list by the length of the string
    lst = sorted(lst)

    return lst