def count_nums(arr):
    nums = [int(i) for i in arr]
    # Iterate through each number and calculate the sum of digits
    # If the sum of digits is greater than 0, the value is set to 1
    # Otherwise, it remains as 0
    return sum(1 for num in nums if sum(int(d) for d in str(abs(num)) if d != '0') > 0)