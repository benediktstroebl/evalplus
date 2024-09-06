
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # 这个函数一开始打算使用range生成a和b之间的整数列表，然后用list comprehension来过滤出它们的偶数部分，但是range并不能给出一个无限长的列表，也就是无法给出从a到b的所有整数
    # 所以我就用了yield来生成一个无限长的迭代器，这样就可以把整个过程从生成一个列表变成了生成一个迭代器，然后在循环中用list()函数把这个迭代器转成列表
    while True:
        if a > b:
            break
        if a % 2 == 0:
            yield a
        a += 1
    return list(generate_integers(a, b))

