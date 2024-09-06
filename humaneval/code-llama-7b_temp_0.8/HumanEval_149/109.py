
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

    def calculate_length(lst):
        """calculate the length of the words in the list"""
        return len(lst)

    def odd_remover(lst):
        """removes words with odd length"""
        return [x for x in lst if len(x) % 2 == 0]

    def odd_length_sort(lst):
        """sort the words by odd length"""
        return sorted(odd_remover(lst), key=lambda x: len(x))

    def even_length_sort(lst):
        """sort the words by even length"""
        return sorted(lst, key=lambda x: len(x))

    # calculate the length of the words in the list
    word_length = calculate_length(lst)
    # create an empty list
    new_list = []
    # sort the words in the list by odd length
    odd_sorted = odd_length_sort(lst)
    # for each word in the odd length list, if the length of the word
    # is the same as the word length, add the word to the new list
    for x in odd_sorted:
        if len(x) == word_length:
            new_list.append(x)
    # sort the words in the new list by even length
    even_sorted = even_length_sort(new_list)
    # return the sorted list
    return even_sorted
