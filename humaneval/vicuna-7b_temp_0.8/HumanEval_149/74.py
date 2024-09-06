
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
    # initialize empty list for sorted list
    sorted_list = []
    
    # for each element in the list
    for word in lst:
        # if the length of the word is odd
        if len(word) % 2 == 1:
            # remove the word from the list
            del lst[lst.index(word)]
            # add the word to the sorted list
            sorted_list.append(word)
    
    # return the sorted list
    return sorted_list