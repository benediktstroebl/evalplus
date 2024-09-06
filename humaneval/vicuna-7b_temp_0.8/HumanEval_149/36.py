
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
    def count_chars(lst):
        """Returns a dictionary of characters in the list and its count."""
        char_count = {}
        for char in lst:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

    def get_max_len(lst):
        """Returns the length of the string with the maximum length in the list."""
        max_len = 0
        max_val = -1
        for char in lst:
            char_count = count_chars(lst)
            if char_count[char] > max_val:
                max_len = char_count[char]
                max_val = char_count[char]
        return max_len

    def sort_lst(lst):
        """Returns the list sorted by its length."""
        sorted_lst = sorted(lst)
        return [item for sublist in sorted_lst for item in sublist]

    max_len = get_max_len(lst)
    sorted_lst = sort_lst(lst)
    for i in range(len(lst)):
        if lst[i][0] != lst[i][1:]:
            sorted_lst.remove(lst[i])
    return sorted_lst
