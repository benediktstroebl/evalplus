def smallest_change(arr):
    ans = float('inf')
    for a in set(arr):
        tem = arr.count(a)
        if tem % 2 == 0:
            continue
        count = 0
        for b in arr:
            if b == a:
                count += 1
        ans = min(ans, count)
    return ans