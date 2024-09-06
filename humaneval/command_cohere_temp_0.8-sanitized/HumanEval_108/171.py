def count_nums(arr):
    return sum(int(b) for b in map(str, arr) if b != '-' and sum(map(int, str(b))) > 0)