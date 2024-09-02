
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
    # Check if the list is empty
    if not lst:
        return []
    
    # Get a copy of the list
    lst = sorted(lst)
    
    # Initialize the result list
    result = []
    
    # Check the length of the first word
    first_word = lst[0]
    if len(first_word) % 2 == 0:
        # Add the first word to the result list
        result.append(first_word)
    
    # Check the length of the next word
    for word in lst[1:]:
        if len(word) % 2 == 0:
            # Add the word to the result list
            result.append(word)
        else:
            # Remove the word from the list
            lst.remove(word)
    
    # Add the remaining words to the result list
    for word in lst:
        if len(word) % 2 == 0:
            # Add the word to the result list
            result.append(word)
    
    # Sort the result list by the length of each word
    result = sorted(result, key=lambda x: (len(x), x))
    
    return result
