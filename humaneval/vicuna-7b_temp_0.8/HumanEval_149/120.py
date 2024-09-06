
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
    # sort the list in ascending order by the length of each word
    lst = sorted(lst)
    # store the first word in the list
    first_word = lst[0]
    # initialize a variable to store the sum
    sum = 0
    # initialize a variable to store the current word
    current_word = first_word
    # iterate through the list and update the sum and current_word
    for i in range(1, len(lst)):
        # if the current word is not the first word
        if i != 0:
            # compare the length of the current word to the first word
            if len(current_word) != len(first_word):
                # if the current word is longer than the first word
                if len(current_word) > len(first_word):
                    # add the current word to the sum
                    sum += current_word
                    # update the current word to the first word
                    current_word = first_word
                # if the current word is shorter than the first word
                else:
                    # add the current word to the sum
                    sum += current_word
                    # update the current word to the first word
                    current_word = first_word
            # if the current word is the first word
            else:
                # add the current word to the sum
                sum += current_word
                # update the current word to the first word
                current_word = first_word
    return [lst[i:j] for i, j in zip(lst, range(len(lst)) + [sum])]
