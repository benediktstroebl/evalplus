
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
    # this list is going to be the list that will be returned
    result = []

    # we can get the length of the list
    list_length = len(lst)

    # we can iterate through each element in the list
    for i in range(list_length):
        # we can get the length of each element
        element_length = len(lst[i])

        # we can check if the length of each element is odd
        if element_length % 2 != 0:
            # if it is odd, we can delete it from the list
            del lst[i]
            # and we can reduce the length of the list by 1
            list_length -= 1

    # we can sort the list
    lst.sort()

    # we can return the list
    return lst
