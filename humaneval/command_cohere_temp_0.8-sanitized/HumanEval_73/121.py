def smallest_change(arr):
    if arr == sorted(arr)[::-1]:
        return 0
    dup = {}
    for i, num in enumerate(arr):
        if num in dup:
            dup[num] += 1
        else:
            dup[num] = 1
    max_dup = max(dup.values())
    return max_dup // 2