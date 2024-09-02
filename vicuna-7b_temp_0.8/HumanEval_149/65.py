
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
    # Get the length of the list
    n = len(lst)
    
    # Initialize an empty list
    result = []
    
    # For each element in the list
    for i in range(n):
        # Get the length of the current element
        length = len(lst[i])
        
        # If the length is even, append the element to the result
        if length % 2 == 0:
            result.append(lst[i])
        
        # If the length is odd, remove the element from the list
        # and append the empty string to the result
        else:
            result.append("")
    
    # Sort the result list in ascending order by the length of each word
    result.sort(key=lambda x: x.count(""))
    
    return result
