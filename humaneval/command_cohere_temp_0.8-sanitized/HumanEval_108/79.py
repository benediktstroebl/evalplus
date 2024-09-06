def count_nums(arr):
    return sum(int(b) >= 0 for a in arr for b in str(a))