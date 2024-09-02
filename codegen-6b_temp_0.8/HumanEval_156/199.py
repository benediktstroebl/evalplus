
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    if number == 0:
        return ""
    def helper(number, result, digits):
        if number < digits:
            return
        elif number == digits:
            result.append(digits[:])
            return
        elif number > digits:
            helper(number, result, digits+1)
            return

        for i in range(len(digits)):
            for j in range(i, len(digits)):
                if i == j:
                    continue

                digits[i], digits[j] = digits[j], digits[i]
                helper(number, result, digits)
                digits[i], digits[j] = digits[j], digits[i]

    counter = [0] * 10
    res = []
    helper(number, res, counter)

    # 这个是为了数字的小写映射
    romans = ['x', 'i', 'v', 'l', 'x', 'c', 'd', 'm']

    l = []
    for r in res:
        n = 10
        for num in r:
            n *= num
        l.append(n)
    l = sorted(l)

    result = ""
    for num in l:
        i = len(l) - 1
        while num > 0:
            result += romans[num % 10]
            num //= 10
            if num != 0:
                result += romans[num % 10]
            i -= 1
            num //= 10
            # print(num)

    return result

