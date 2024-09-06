
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
    # sort the list by the length of the word
    sorted_lst = sorted(lst, key=len, reverse=True)
    # create an empty list to store the length of each word
    length_lst = [0] * (len(lst) + 1)
    # iterate over the sorted list
    for word in sorted_lst:
        # if the length of the word is odd
        if len(word) % 2 == 1:
            # increment the length of each word by 1
            length_lst[len(word) // 2] += 1
    # concatenate the sorted list with the list of word lengths
    result = [word] + length_lst
    return result