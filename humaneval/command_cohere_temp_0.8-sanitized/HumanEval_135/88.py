def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, cur in enumerate(arr):
        if cur > prev:
            return -1
        elif cur <= prev and idx > 0 and arr[idx - 1] <= arr[idx]:
            continues = True
            arr_tmp = arr[idx:]
            prev_tmp = arr[idx - 1]
            for i in range(idx + 1, len(arr_tmp)):
                if arr_tmp[i] > prev_tmp:
                    continues = False
                    break
            if continues:
                arranges.append(idx)
        prev = cur
    if arranges:
        return max(arranges)
    else:
        return -1