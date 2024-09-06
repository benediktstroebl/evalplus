def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)