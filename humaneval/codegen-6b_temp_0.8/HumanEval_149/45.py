
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
    #  O(n log n)
    """
    result = []
    for word in lst:
        if len(word) % 2 == 0:
            result.append(word)
    return sorted(result, key=len)
    """
    #  O(n)
    left, right = 0, len(lst) - 1
    while left < right:
        if len(lst[left]) % 2 != 0:
            del lst[left]
            right -= 1
        else:
            left += 1
    return sorted(lst, key=len)

