
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        return n
    else:
        nums = []
        while n > 10:
            nums.append(n % 10)
            n = n // 10
            if n == 0:
                nums.append(n)
        if n % 2 == 0:
            return 0
        else:
            nums.append(n)
        nums = [x for x in nums if x % 2 != 0]
        product = 1
        for num in nums:
            product = product * num
        return product
