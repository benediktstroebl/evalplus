
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
    # List to store the strings that have odd length
    odd_lst = []
    # List to store the sorted strings
    sorted_lst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            # Append the string to the sorted_lst
            sorted_lst.append(lst[i])
        else:
            # Append the string to the odd_lst
            odd_lst.append(lst[i])
    # Combine the sorted_lst and odd_lst
    combined_lst = sorted_lst + odd_lst
    # Sorted the list by length of each word
    sorted_combined_lst = sorted(combined_lst, key=lambda x: len(x))
    # Return the sorted list
    return sorted_combined_lst