def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        elif n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
        max_val = max(max_val, n)
    for n in freq:
        if freq[n] >= n:
            return n
    return -1