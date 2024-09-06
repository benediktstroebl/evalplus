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
    return -1 if max_val == 0 else max(k for k, v in freq.items() if k >= v)