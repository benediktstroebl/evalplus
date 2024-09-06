
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
    # use a helper variable to keep track of the running sum
    # initialize it to 0
    running_sum = 0
    
    # loop through the list
    for word in lst:
        # if the word is not empty and the length is odd,
        # add the word to the list and increase the running sum by 1
        if len(word) > 0 and len(word) % 2 == 1:
            running_sum += word
            lst.remove(word)
        else:
            # if the word is not empty and the length is even,
            # add the word to the list if it is not already in the list,
            # increase the running sum by 1,
            # and remove the word if it is in the list
            if word not in lst:
                running_sum += word
                lst.append(word)
            else:
                running_sum += word
    
    # return the sorted list
    return lst
