def pluck(arr):
    arr.sort()
    if not arr or not arr[0] % 2:
        return []
    return [arr[0] // 2, arr[0] // 2]