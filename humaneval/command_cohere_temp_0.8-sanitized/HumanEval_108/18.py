def count_nums(arr):
    nums = [int(i) for i in arr]
    # Calculate the sum of digits for each number
    # If negative, the first digit is considered as -1
    # and removed from the sum as it contributes +1 to the overall sum
    cnt = sum(sum(list(str(n))) for n in nums if str(n)[0] != '-')
    return len(nums) - cnt