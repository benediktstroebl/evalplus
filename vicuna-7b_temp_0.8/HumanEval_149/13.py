
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
    lst = sorted(lst)
    while lst:
        if lst[0].isdigit():
            start_index = 0
            for i in range(1, len(lst)):
                if lst[i].isdigit() == False:
                    start_index = i
                    break
            if start_index == 0:
                lst.pop(0)
                continue
            for i in reversed(range(start_index, len(lst))):
                if lst[i].isdigit() == False:
                    break
            else:
                del lst[start_index]
        elif lst[0].isalpha():
            start_index = 0
            for i in range(1, len(lst)):
                if lst[i].isalpha() == False:
                    start_index = i
                    break
            if start_index == 0:
                lst.pop(0)
                continue
            for i in reversed(range(start_index, len(lst))):
                if lst[i].isalpha() == False:
                    break
            else:
                del lst[start_index]
        else:
            start_index = 0
            for i in range(1, len(lst)):
                if lst[i] == lst[i-1] == False:
                    start_index = i
                    break
            if start_index == 0:
                lst.pop(0)
                continue
            for i in reversed(range(start_index, len(lst))):
                if lst[i] == lst[i-1] == False:
                    del lst[i]
    return lst