def specialFilter(nums):
    odd_count = 0
    odd_first_digit = 0
    odd_last_digit = 0

    for num in nums:
        if int(num[0]) > 10 or int(num[-1]) > 10:
            odd_count += 1
        if int(num[0]) % 2 == 1 and int(num[-1]) % 2 == 1:
            odd_first_digit += 1
        if int(num[-1]) % 2 == 1 and int(num[0]) % 2 == 1:
            odd_last_digit += 1

    return odd_count, odd_first_digit, odd_last_digit