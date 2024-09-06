
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Your code here
    sum = 0
    flag = False
    for i in range(1, n, 2):
        if n - i < 0:
            flag = True
            break
        for j in range(1, n, 2):
            if n - i - j < 0:
                flag = True
                break
            for k in range(1, n, 2):
                if n - i - j - k < 0:
                    flag = True
                    break
                for l in range(1, n, 2):
                    if n - i - j - k - l == 0:
                        return True
    return False
