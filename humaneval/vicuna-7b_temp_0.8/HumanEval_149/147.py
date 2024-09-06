
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
    # sort the list in ascending order
    lst = sorted(lst)
    # create a variable to keep track of the current index
    current_index = 0
    # create a variable to keep track of the current length
    current_length = 1
    # loop through the list
    for i in range(len(lst)):
        # check if the current length is odd
        if current_length % 2 == 1:
            # if the length is odd, remove it and decrement the index
            lst.remove(lst[i])
            current_index -= 1
        else:
            # if the length is even, check if it is greater than the current
            # length and if it is, increment the current length and the index
            if current_length < lst[i]:
                current_length += 1
                current_index += 1
        # check if the current index is out of bounds
        if current_index < 0:
            current_index = 0
        elif current_index >= len(lst):
            current_index = len(lst) - 1
    return lst
