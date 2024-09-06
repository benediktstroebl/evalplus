
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a = n//2
    b = a
    while a <= b and a+b <= n:
        if (a+b) % 2 == 0:
            c = (n-a-b)//2
            d = c
            while c <= d:
                if (a+b+c+d) == n:
                    return True
                c += 1
        a += 1
    return False
