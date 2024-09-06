def count_nums(arr):
    output = sum(int(n) for n in arr if sum(map(int, str(n))) > 0)
    return output