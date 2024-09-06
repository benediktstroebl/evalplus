
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
    from collections import Counter

    middle = len(arr) // 2
    freq = Counter(arr[:middle])
    ans = 0
    for i in range(middle, len(arr)):
        if arr[i] in freq:
            freq[arr[i]] -= 1
            if freq[arr[i]] == 0:
                del freq[arr[i]]
        else:
            ans += 1
    return ans + middle - len(freq)

