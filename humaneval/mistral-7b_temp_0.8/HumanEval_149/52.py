
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
    # Your code here...

    def sort_by_length(a, b):
        return (len(a) - len(b))

    def sort_by_alphabet(a, b):
        return (a < b)

    if not isinstance(lst, list):
        return lst

    res = list(filter(lambda x: len(x) % 2 == 0, lst))
    res.sort(key=sort_by_length)
    res.sort(key=sort_by_alphabet)
    return res
