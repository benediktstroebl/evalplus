
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
    # initialize two empty lists
    odd_lst = []
    sorted_lst = []

    for word in lst:
        # check the length of the word
        if len(word) % 2 == 0:
            # if the word is even, append it to the sorted_lst
            sorted_lst.append(word)
        else:
            # if the word is odd, append it to the odd_lst
            odd_lst.append(word)

    # remove duplicates from the odd_lst
    odd_lst = list(set(odd_lst))

    # concatenate the sorted_lst and the odd_lst
    concatenated_lst = sorted_lst + odd_lst

    # sort the concatenated_lst by the length of the words
    concatenated_lst = sorted(concatenated_lst, key=lambda x: len(x), reverse=True)

    return concatenated_lst
