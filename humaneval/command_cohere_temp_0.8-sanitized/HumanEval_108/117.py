def count_nums(arr):
    nums = [int(i) for i in arr]
    # Counter to count the numbers with positive sum of digits
    count = 0
    for num in nums:
        if num < 0:
            # Check if number is negative
            num = -num
            # Remove negative sign and count if the number becomes positive
            if num > 0:
                count += 1
        elif num > 0:
            # If positive number, add 1 to the count
            count += 1
    return count