def count_nums(arr):
    output = sum(int(b) for b in map(str, arr) if b != '-')
    return output