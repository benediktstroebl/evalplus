def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for i, val in enumerate(arr):
        if val > prev:
            return -1
        if val <= prev and i > 0:
            continues = 1
            for j in range(i-1, -1, -1):
                if arr[j] <= arr[j+1]:
                    continues += 1
                else:
                    break
            if continues == len(arr) - i:
                arranges.append(i)
        prev = val
    arranges.sort()
    return max(arranges) if arranges else -1