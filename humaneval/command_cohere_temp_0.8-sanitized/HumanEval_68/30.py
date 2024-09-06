import time
def pluck(arr):
    if not arr or not isinstance(arr, list):
        return []
    if arr and arr[0] % 2 == 0:
        return [arr[0], 0]
    ev = [x for x in arr if x % 2 == 0]
    if not ev:
        return []
    return [min(ev), min(range(len(arr)), key=lambda x: (ev.index(arr[x]), x))]