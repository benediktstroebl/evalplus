
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
    # If the length of the list is smaller than 2 then return the list as is.
    if len(lst) < 2:
        return lst

    # The sorted function returns a list,
    # therefore no need to return a list of a list.
    return sorted(
        sorted(lst, key=len),
        key=lambda x: x if len(x) % 2 == 0 else "",
        reverse=True,
    )

