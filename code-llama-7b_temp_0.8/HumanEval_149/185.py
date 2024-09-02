
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

    if len(lst) <= 0:
        return lst

    if len(lst) == 1:
        return lst

    # find the minimum word
    min_word = lst[0]
    for word in lst:
        if len(word) < len(min_word):
            min_word = word

    # find the index of the minimum word
    min_index = 0
    for index, word in enumerate(lst):
        if word == min_word:
            min_index = index
            break

    # find the second minimum word
    sec_min_word = lst[min_index + 1]
    for word in lst[min_index + 1:]:
        if len(word) < len(sec_min_word):
            sec_min_word = word

    # find the index of the second minimum word
    sec_min_index = min_index + 1
    for index, word in enumerate(lst[min_index + 1:]):
        if word == sec_min_word:
            sec_min_index = index + min_index + 1
            break

    # swap the minimum word with the second minimum word
    lst[min_index], lst[sec_min_index] = lst[sec_min_index], lst[min_index]

    return sorted_list_sum(lst[:min_index + 1]) + sorted_list_sum(lst[min_index + 1:])
