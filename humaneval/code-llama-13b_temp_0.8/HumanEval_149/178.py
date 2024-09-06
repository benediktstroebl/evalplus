
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

    """
    [algo]
    I. filter out strings with odd length
    II. sort strings by length, ascending

    [input]
    @lst: a list of strings

    [output]
    @lst: a list of strings
    """
    # FILTER
    # A. get all elements with even length
    even_len = filter(lambda x: len(x) % 2 == 0, lst)
    # B. sort by length ascending
    res = sorted(even_len, key=lambda x: (len(x), x))

    return res
