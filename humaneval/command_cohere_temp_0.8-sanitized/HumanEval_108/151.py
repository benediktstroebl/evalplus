def count_nums(arr):
    nums = [int(i) for i in arr]
    # Count numbers with positive digit sum
    count = sum(1 for num in nums if sum(int(d) for d in str(num)) > 0)
    return count