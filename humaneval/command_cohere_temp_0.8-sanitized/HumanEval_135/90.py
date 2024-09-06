def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, ele in enumerate(arr):
        if ele > prev:
            return -1
        elif ele == prev:
            continues = 1
            while continues < len(arr) and arr[continues] == prev:
                continues += 1
            if continues == idx + 1:
                arranges.append(idx)
            else:
                arranges.append(-1)
        prev = ele
    return max(arranges)