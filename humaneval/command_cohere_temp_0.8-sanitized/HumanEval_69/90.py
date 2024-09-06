def search(lst):
    freq, max_val = -1, 0
    for i in lst:
        if i > 0 and i >= freq:
            max_val, freq = i, 1
        elif i > 0 and freq < i:
            freq += 1
        elif i == 0:
            freq += 1
        else:
            continue
    return max_val if max_val >= 0 else -1