def count_nums(arr):
    if not arr:
        return 0
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output