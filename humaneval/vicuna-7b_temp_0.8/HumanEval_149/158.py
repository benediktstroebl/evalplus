
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
    # Define the result variable as an empty list
    result = []
    
    # Use a for loop to iterate over the list
    for word in lst:
        # Check if the length of the word is odd
        if len(word) % 2 == 1:
            # Remove the word from the list
            result.remove(word)
        else:
            # Add the word to the result list
            result.append(word)
    
    # Sort the result list by the length of each word
    result = sorted(result, key=lambda x: (len(x), x))
    
    return result