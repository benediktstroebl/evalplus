def search(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return max(freq)
lst = [4, 1, 2, 2, 3, 1]