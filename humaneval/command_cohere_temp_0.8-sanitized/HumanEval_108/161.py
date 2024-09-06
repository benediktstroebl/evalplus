def count_nums(arr):
    output = sum(int(b) for b in map(lambda x: str(abs(x)), arr) if sum(map(int, str(abs(x)))) > 0)
    return output