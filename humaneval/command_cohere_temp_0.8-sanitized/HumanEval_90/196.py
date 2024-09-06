def next_smallest(lst):
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left == len(arr)

    lst.sort()
    if not lst or lst[0] == lst[1]:
        return None
    elif len(lst) < 2 or lst[1] == lst[2]:
        return lst[1]
    else:
        repeat = lst[1]
        start = 1
        while start < len(lst) - 1 and lst[start] == repeat:
            start += 1
        if not start < len(lst) - 1:
            return None
        return lst[start + 1]