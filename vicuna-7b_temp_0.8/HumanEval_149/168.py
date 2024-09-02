
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
    # sort the list by the length of each string
    lst = sorted(lst, key=len, reverse=True)

    # create a set of all the strings in the list
    seen = set()
    lst2 = []
    for string in lst:
        if string not in seen:
            seen.add(string)
            lst2.append(string)

    # remove the duplicates and sort the resulting list
    lst2 = list(lst2)
    return [string for string in lst2 if len(string) % 2 == 0 and string not in seen]

lst = ["aa", "a", "aaa"]
lst2 = sorted_list_sum(lst)
