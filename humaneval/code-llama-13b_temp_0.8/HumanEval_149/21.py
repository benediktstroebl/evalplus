
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
    # validating if the input is a list
    if not isinstance(lst, list):
        return "Input must be a list."
    # validating if all values in the list are strings
    if not all([isinstance(x, str) for x in lst]):
        return "Not all values in the list are strings."
    # returning the valid list
    return sorted(list(filter(lambda x: len(x) % 2 == 0, lst)), key=len)
