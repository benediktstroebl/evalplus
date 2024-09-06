
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
    
    # create an empty list to store the result
    result = []
    
    # iterate over the list
    for item in lst:
        # get the length of the item
        length = len(item)
        
        # check if the length is even
        if length % 2 == 0:
            # add the item to the result list
            result.append(item)
        else:
            # if the length is odd, remove the item from the list
            lst.remove(item)
    
    # return the result list
    return result
