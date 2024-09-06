
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

    # Write your code here!
    freq = {}
    for e in arr:
        if e in freq:
            freq[e] += 1
        else:
            freq[e] = 1

    min_odd_freq = 9999999999
    for e in freq:
        if freq[e] % 2 == 1:
            min_odd_freq = min(min_odd_freq, freq[e])

    odd_freq = min_odd_freq if min_odd_freq != 9999999999 else 0
    palindrome_list = []
    for e in freq:
        if freq[e] % 2 == 0:
            palindrome_list.append(e * (freq[e] // 2))
        else:
            palindrome_list.append((e * (freq[e] // 2)) + e)

    palindrome_list = sorted(palindrome_list)
    return len(palindrome_list) + odd_freq

