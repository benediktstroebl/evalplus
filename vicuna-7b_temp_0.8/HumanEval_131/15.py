
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # https://leetcode.com/problems/digits/description/
    # 找到了解考前的代码，这里使用了字典依次排序的方式
    # 可以使用一个假设 n 的最大整数为 10^9 + 7
    # 从小到大排序，并在排序的过程中检查 n 的模
    # 如果模小于 3，则 n 的前两位都是奇数
    # 对于 n 的模大于等于 3，可以使用字典排序得到最快的排序方式
    # 这里使用了字典的内置方法dict.items() 来获取字典的元素，而
    # 使用了字典的反样行的方式来排序字典的元素，得到到
    # 最快的排序方式
    digits = 0
    for key in sorted(dict.items(n // 10)):
        digits *= int(key)
    if n % 2 == 0:
        return 0
    return digits
