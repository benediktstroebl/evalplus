
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Your code here
    if n % 2 == 0:
        s = 0
        for i in range(2, n + 1, 2):
            if n - i <= 0:
                break
            if n - 2*i <= 0:
                break
            if n - 3*i <= 0:
                break
            if n - 4*i <= 0:
                break
            s += i
            if s == n:
                return True
    return False
