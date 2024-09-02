
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    s = str(n)
    s = s.zfill(9)
    result = True
    for i in range(len(s)-3):
        if int(s[i]) + int(s[i+2]) > int(s[i+1]):
            result = False
            break
    return result
