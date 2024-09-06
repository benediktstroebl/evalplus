def count_nums(arr):
    output = sum(int(b) for a in arr for b in str(a) if b != '-' and int(b) > 0)
    return output