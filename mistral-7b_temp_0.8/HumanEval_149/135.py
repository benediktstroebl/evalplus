
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

    def odd_words(lst):
        """
        returns a list of odd words from the list of words
        """
        words = []
        for word in lst:
            if len(word) % 2 != 0:
                words.append(word)
        return words

    def length_sort(lst):
        """
        returns a list sorted by length of words
        """
        new_lst = []
        for word in lst:
            if len(word) not in new_lst:
                new_lst.append(len(word))
        for word in lst:
            if len(word) == new_lst[0]:
                new_lst.append(word)
                new_lst.remove(new_lst[0])
        return new_lst

    def alphabet_sort(lst):
        """
        returns a list sorted alphabetically
        """
        for i in range(0, len(lst)):
            for j in range(i, len(lst)):
                if lst[i] > lst[j]:
