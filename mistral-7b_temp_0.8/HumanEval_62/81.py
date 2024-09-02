

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # 需要注意的点是
    # 1. 这个xs是一个list，但是list内部的元素是数字
    # 2. 这个xs是一个列表，但是list内部的元素是numbers
    # 需要注意的点是，xs是一个list，它的每个元素是个number，而number有个pow函数
    # 由于其他语言的缘故，要表达上面的想法，有时候要用'str'，有时候要用'string'，有时候用'字符串'
    # 我想python的文档好像是更加友好一些，如果一个元素是个字符串，或者list的元素是个字符串，
    # 那么如果把它转换成list，那么list里的元素依然是个字符串
    # 但是如果把它转换成tuple，那么tuple里的元素依然是个字符串
    # 如果把它
