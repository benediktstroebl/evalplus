
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4 != 0:
        return False
    else:
        l = [1, 3, 7, 9]
        for i in range(2, n):
            if i % 4 == 0:
                l.append(i)
        for i in range(1, len(l)):
            if l[i] - l[i - 1] != 2:
                return False
        return True

