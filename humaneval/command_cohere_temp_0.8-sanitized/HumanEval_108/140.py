def count_nums(arr):
    nums = [int(i) for i in arr]
    # Define a variable to store the count of numbers with positive digit sum.
    count = 0
    for num in nums:
        if num < 0:
            # If the number is negative, we consider the absolute value of the number and subtract 1 from the sum of digits.
            digits = abs(num)
            sum_of_digits = sum(map(int, str(digits))) - 1
        else:
            # If the number is positive, we calculate the sum of digits normally.
            digits = num
            sum_of_digits = sum(map(int, str(digits)))
        if sum_of_digits > 0:
            count += 1
    return count