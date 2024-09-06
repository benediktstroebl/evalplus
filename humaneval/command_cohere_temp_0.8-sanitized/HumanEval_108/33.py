def count_nums(arr):
    output = sum(int(num) >= 0 for num in arr)
    return output