
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 != 0:
        return False

    sum = 0
    found = False
    for i in xrange(4, int(n/2) if n%4==0 else n/2+1, 2):
        if sum+i <= n:
            sum += i
        else:
            if sum == n:
                found = True
                break
            else:
                break

    return found

