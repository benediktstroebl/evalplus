
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # build a character count dictionary
    cnt = {}
    for i in arr:
        if i not in cnt:
            cnt[i] = 0
        cnt[i] += 1
    if len(cnt.keys()) == 1:
        return 0
    # find the minimum characters by iterating over the keys
    min_char = None
    for i in cnt:
        if min_char is None or cnt[i] < cnt[min_char]:
            min_char = i
    # find the characters that don't match the min
    chars = list(cnt.keys())
    chars.remove(min_char)
    res = 0
    for i in chars:
        res += (cnt[i] - cnt[min_char])
    return res

