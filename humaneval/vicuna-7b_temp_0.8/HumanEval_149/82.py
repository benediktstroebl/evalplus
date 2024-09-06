
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
    # sort the list alphabetically by word length
    lst = sorted(lst)
    
    # check if the list is empty
    if not lst:
        return []
    
    # check if the list is a single string
    if not lst[0].isalpha():
        return [""]
    
    # initialize an empty list to store the unique strings
    unique_lst = []
    
    # loop through the list and add the non-empty strings to the unique_lst list
    for word in lst:
        if len(word) > 0:
            unique_lst.append(word)
    
    # return the unique_lst list, which contains only strings with non-empty length
    return unique_lst
