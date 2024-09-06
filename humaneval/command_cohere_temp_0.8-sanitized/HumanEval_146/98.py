def specialFilter(nums):
    odd_digits = [x for x in nums if int(x) > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(odd_digits)