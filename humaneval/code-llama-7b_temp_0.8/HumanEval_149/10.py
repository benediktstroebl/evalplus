
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

    odd_words = []
    even_words = []
    sorted_even_words = []
    sorted_odd_words = []
    lst_sorted = []

    for word in lst:
        if len(word) % 2 == 0:
            even_words.append(word)
        else:
            odd_words.append(word)

    even_words.sort()
    odd_words.sort()

    sorted_even_words = even_words
    sorted_odd_words = odd_words

    sorted_words = sorted_even_words + sorted_odd_words

    return sorted_words

