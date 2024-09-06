def search(nums):
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    for n in freq:
        if freq[n] >= n:
            return n
    return -1