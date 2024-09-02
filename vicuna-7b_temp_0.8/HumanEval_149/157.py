
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
    # How to sort the list
    def sort_helper(lst, index, length):
        if index == len(lst) - 1:
            # If we reach the end of the list,
            # we return the sorted list
            return lst

        for i in range(index + 1, len(lst)):
            if len(lst[index]) < len(lst[i]):
                # If the current element has a length that is smaller
                # than the next element, we swap them
                lst[index], lst[i] = lst[i], lst[index]

        return lst

    sorted_lst = []
    for word in lst:
        length = len(word)
        if length % 2 == 0:
            # If the length of the word is even,
            # it is a valid word and can be added to the sorted list
            sorted_lst.append(word)
        else:
            # If the length of the word is odd,
            # it is an invalid word and must be skipped
            pass

    # After removing all invalid words,
    # we sort the remaining words alphabetically by length
    sorted_lst = sort_helper(sorted_lst, 0, len(sorted_lst[-1]))

    return sorted_lst