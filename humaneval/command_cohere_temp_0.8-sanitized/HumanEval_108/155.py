def count_nums(arr):
    num_sum = sum([int(n) for n in map(str, arr) if int(n) < 0])
    return len(arr) - num_sum