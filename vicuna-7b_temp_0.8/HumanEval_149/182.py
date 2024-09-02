
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
    # This is the O(n) solution, where n is the number of elements in the list.
    # The idea is to use a queue to keep track of the elements in the list, and
    # to repeatedly dequeue an element until the queue is empty, and then return
    # the list with the remaining elements.
    #
    # We keep track of the maximum length of all elements in the list using a variable
    # called max_len. If an element has an odd length, we update max_len and
    # then append it to a new list called new_lst.
    #
    # The function then returns new_lst, which will be sorted by length and then
    # alphabetically if two elements have the same length.

    max_len = max([len(word) for word in lst])
    new_lst = []
    for word in lst:
        if len(word) % 2 == 0:
            new_lst.append(word)
        else:
            new_lst.append((len(word), word))
    new_lst = sorted(new_lst, key=lambda x: x[1])
    return new_lst