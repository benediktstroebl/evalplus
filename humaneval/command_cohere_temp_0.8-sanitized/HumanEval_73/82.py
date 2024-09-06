def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    return min(odd, len(arr) - odd)