def count_nums(arr):
    nums = [int(i) for i in arr]
    # Calculating the sum of digits and checking if it's greater than 0
    return sum(1 for num in nums if sum(int(d) for d in str(abs(num)) if d.isdigit()) > 0)