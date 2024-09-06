def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, ele in enumerate(arr):
        if ele <= prev:
            continues = True
            for i in range(idx + 1, len(arr)):
                if arr[i] > ele:
                    continues = False
                    break
            if continues:
                arranges.append(idx)
        prev = ele
    return max(arranges, default=-1)