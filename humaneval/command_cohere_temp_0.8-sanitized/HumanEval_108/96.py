def count_nums(arr):
    nums = [int(i) for i in arr]
    # Iterate through each number and check if their digit sum is greater than 0
    return sum(1 for num in nums if sum(int(d) for d in str(num)) > 0)