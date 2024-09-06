def count_nums(arr):
    return sum(sum(map(int, str(x))) > 0 for x in arr)