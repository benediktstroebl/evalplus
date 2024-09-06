

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # 需要首先将数字序列转化为多项式
    # 即将[1, 2, 3]转化为 1 + 2x + 3x^2
    # 这个转化的过程在多项式算法的多项式推导中已经有了很好的实现
    # 注意1 + 2x + 3x^2 是一个多项式，每一项是一个整数
    # 这个转化的过程也可以用递归来实现，见如下代码
    # 该代码用于从数字序列中获得多项式
    def get_polynomial(xs, x_power=1):
        if len(xs) == 0:
            return 0
        if xs[0] == 0:
            return 0
        if len(xs) == 1:
            return xs[0] * x_power
        return xs[0] * x_power + get_polynomial(xs[1:], x
