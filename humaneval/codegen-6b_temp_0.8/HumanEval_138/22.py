
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    def find_quadruple(n):
        """Return a quadruple of 3 consecutive positive integers that sum up to n.
        """
        quadruple = None
        for i in xrange(1, n):
            for j in xrange(i+1, n - 1):
                k = n - i - j
                if (i + j + k) == n:
                    quadruple = i, j, k
                    break
            if quadruple:
                break
        return quadruple
    quadruple = find_quadruple(n)
    return quadruple and sum(quadruple) % 2 == 0
