def count_nums(arr):
    nums = [int(i) for i in arr]
    # Filter out numbers with digit sum <= 0
    filtered = [i for i in nums if sum(int(c) for c in str(i)) > 0]
    return len(filtered)