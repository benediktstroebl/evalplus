
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
    # Find the sorted list
    sorted_list = []
    sorted_list_index = 0
    for word in lst:
        if word == "":
            continue
        elif sorted_list_index == len(lst) - 1:
            sorted_list.append(lst[sorted_list_index])
            break
        elif len(word) > len(lst[sorted_list_index]):
            sorted_list.insert(sorted_list_index, word)
            sorted_list_index += 1
        elif len(word) < len(lst[sorted_list_index]):
            sorted_list.insert(sorted_list_index, word)
            sorted_list_index += 1
            if sorted_list_index == len(lst) - 1:
                sorted_list.append(lst[sorted_list_index])
                break
        else:
            sorted_list.insert(sorted_list_index, word)
            sorted_list_index += 1
    return sorted_list