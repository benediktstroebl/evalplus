
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
    # Use a dictionary to store unique words in sorted order
    unique_words = {}

    for word in lst:
        if word in unique_words:
            unique_words[word] = len(word) + 1
        else:
            unique_words[word] = 1

    # Delete words that have odd lengths
    sorted_lst = []
    for word in unique_words:
        if word % 2 == 0:
            sorted_lst.append(word)

    return sorted_lst
