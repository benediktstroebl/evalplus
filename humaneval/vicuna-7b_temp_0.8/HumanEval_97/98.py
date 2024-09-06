
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # 将两个数字分别作为不同的变量
    a_digits = str(a).split('.')
    b_digits = str(b).split('.')

    # 将每个数字的千位分别作为变量
    a_thousand_digits = a_digits[0]
    b_thousand_digits = b_digits[0]

    # 计算两个数字的千位和分位的和
    a_sum = int(a_thousand_digits + b_thousand_digits)
    b_sum = int(b_thousand_digits)

    # 将分位数字作为一个变量，将千位数字作为其它变量
    thousands_digit = str(b_sum)
    rest_digit = str(a_sum - int(b_sum))

    # 将剩余的数字作为另一个变量，并返回它们的乘积
    rest_sum = int(rest_digit + thousands_digit)
    product_sum = multiply(a_sum, b_sum)

    # 将乘积的结果，最后进行正则化
    product_str = str(product_sum)
    product = int(product_str[0])

    # 将乘积的结果作为一个字符串返回
    return product