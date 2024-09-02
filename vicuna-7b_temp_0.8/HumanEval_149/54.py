
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
    def repl(lst):
        if lst:
            return lst[0]
        return lst[0]
    result = []
    i = 0
    j = 0
    while i < len(lst):
        if j + 1 >= len(lst):
            break
        if len(lst[i]) != len(lst[j]):
            # Insert space between the strings
            result.append(lst[i])
            result.append(lst[j])
            i += 1
            j += 1
        elif lst[i] != repl(lst[j]):
            # Insert space between the strings
            result.append(lst[i])
            result.append(lst[j])
            i += 1
            j += 1
        else:
            result.append(lst[i])
            i += 1
    result = sorted(result, key=lambda x: x.count(" "))
    return result
