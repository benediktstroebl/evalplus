
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
    
    # Initialize an empty list to store the result
    result = []
    
    # Sort the list by the length of each word
    lst.sort(key=lambda x: len(x))
    
    # Create a set to keep track of the unique words in the list
    unique_words = set()
    
    # Iterate through the list
    for word in lst:
        # If the word is already in the set, ignore it
        if word in unique_words:
            continue
        # If the word is not in the set, add it and increment the count
        unique_words.add(word)
        result.append(word)
    
    # Return the sorted list
    return result

lst = ["aa", "a", "aaa", "aa", "a", "aaa", "bb", "b", "bbb", "bb"]
