def count_nums(arr):
    return sum(int(b) for b in map(str, arr) if b != '-' and sum(int(d) for d in str(b)) > 0)