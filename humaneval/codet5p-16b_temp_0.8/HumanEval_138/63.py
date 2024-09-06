
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = int(n)
    if n <= 0:
        return False
    elif n % 2 == 0:
        return False
    else:
        result = 0
        for i in range(1,n):
            if result + i % 2 == 0:
                result += i
            elif result + i % 2!= 0:
                result += i
                if result == n:
                    return True
                elif result > n:
                    return False
            else:
                return False
        return False
