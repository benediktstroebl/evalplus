
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
    counts = Counter(arr)
    freqs = [(value, count) for count, value in counts.items()]
    freqs.sort()
    freqs.reverse()
    freq, max_freq = freqs[0]
    if freq == 1:
        return len(freqs)
    for value, count in freqs[1:]:
        if count == freq:
            freq = count * max_freq
            break
    else:
        freq = max_freq
    result = (len(freqs) - 1) * freq
    for value, count in freqs:
        if count < freq:
            result += freq - count
    return result

