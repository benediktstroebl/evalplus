
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
    # sort the list
    lst = sorted(lst)
    # initialize the result list
    result = []
    # check if the list is empty
    if not lst:
        return result
    # check the first word
    first_word = lst[0]
    # add the first word to the result list
    result.append(first_word)
    # check if the list has only one word
    if len(lst) == 1:
        return result
    # check the remaining words
    for word in lst[1:]:
        # check if the word is equal to the first word
        if word == first_word:
            continue
        # check if the word is longer than the first word
        if len(word) > len(first_word):
            result.append(word)
    return result
