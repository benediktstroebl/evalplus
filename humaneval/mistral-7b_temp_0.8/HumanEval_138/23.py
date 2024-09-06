
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    s = set([2, 4, 6, 8])
    l = []
    while n:
        l.append(n % 10)
        n = n // 10
    l = l[::-1]
    sum_l = 0
    for i in range(len(l)):
        sum_l += l[i]
    if sum_l in s:
        return True
    else:
        return False
