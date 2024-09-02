
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
    # 1. Get the list of strings
    list_of_strings = lst

    # 2. Iterate over the list of strings
    for i in range(len(list_of_strings)):
        # 2.1. Get the current word
        word = list_of_strings[i]
        # 2.2. Check if the word is odd
        if word.count(".") % 2 != 0:
            # 2.2.1. Add the word to the new list
            new_list = list(word) + [word]

            # 2.2.2. Remove the word from the original list
            list_of_strings.remove(word)

            # 2.2.3. Add the word back to the original list
            list_of_strings.insert(i, word)
        else:
            # 2.2.3. Add the word to the new list
            new_list.append(word)

    # 3. Sort the new list
    return sorted(new_list, key=lambda x: len(x))
