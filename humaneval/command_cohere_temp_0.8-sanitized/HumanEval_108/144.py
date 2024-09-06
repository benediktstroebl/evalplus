def count_nums(arr):
    num_sum = 0
    for n in arr:
        s = str(n)
        if s[0] != '-' and sum(int(d) for d in s) > 0:
            num_sum += 1
    return num_sum