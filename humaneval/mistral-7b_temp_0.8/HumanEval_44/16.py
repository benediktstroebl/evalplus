

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # base, x = x, base
    # result = ""
    # while base <= x:
    #     # result = str(x % base) + result
    #     x = x // base
    #     # print("x: ", x)
    #     # print("result: ", result)
    # result = str(x) + result
    # print("result: ", result)
    # return result

    # return "".join(str(x % base) for x in reversed(range(10, 0, -base)))
    # base = 10
    # result = ""
    # while base <= x:
    #     # result = str(x % base) + result
    #     x = x // base
    #     # print("x: ", x)
    #     # print("result: ", result)
    # result = str(x) + result
    # print("result: ", result)
    # return result

    # return "".join(str(x % base) for x in reversed(range(10, 0, -base
