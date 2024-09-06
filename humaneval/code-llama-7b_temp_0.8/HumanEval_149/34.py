
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
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if len(lst[0]) == len(lst[1]):
            if lst[0] < lst[1]:
                return lst
            else:
                return lst[::-1]
        else:
            return [lst[0]] if len(lst[0]) < len(lst[1]) else [lst[1]]
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        left_sorted = sorted_list_sum(left)
        right_sorted = sorted_list_sum(right)
        left_sorted_len = len(left_sorted)
        right_sorted_len = len(right_sorted)
        result = []
        left_index = 0
        right_index = 0
        while left_index < left_sorted_len and right_index < right_sorted_len:
            if len(left_sorted[left_index]) == len(right_sorted[right_index]):
                if left_sorted[left_index] < right_sorted[right_index]:
                    result.append(left_sorted[left_index])
                    left_index += 1
                else:
                    result.append(right_sorted[right_index])
                    right_index += 1
            elif len(left_sorted[left_index]) < len(right_sorted[right_index]):
                result.append(left_sorted[left_index])
                left_index += 1
            else:
                result.append(right_sorted[right_index])
                right_index += 1
        result += left_sorted[left_index:]
        result += right_sorted[right_index:]
        return result

