
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
    # Step 1: Create a new list to store the sorted strings
    new_lst = []
    # Step 2: Iterate through the original list of strings
    for word in lst:
        # Step 3: If the word has an odd length, append it to the new list
        if len(word) % 2 != 0:
            new_lst.append(word)
        # Step 4: If the word does not have an odd length, check if the word is already in the new list
        else:
            # Step 5: If the word is in the new list, append it to the new list
            if word not in new_lst:
                new_lst.append(word)
            # Step 6: If the word is not in the new list, append it to the new list
            else:
                new_lst.append(word)
    # Step 7: Return the sorted list
    return new_lst
