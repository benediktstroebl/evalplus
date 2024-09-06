def count_nums(arr):
    nums = [int(i) for i in arr]
    counts = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            counts += 1
    return counts