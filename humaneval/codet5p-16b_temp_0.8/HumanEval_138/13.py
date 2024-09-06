
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    import math
    
    if n%2 == 0:
        return False
    else:
        if int(math.sqrt(n)) == math.sqrt(n):
            return False
        else:
            possible_sums = []
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    if (i % 2 == 0) and (n // i <= 4):
                        possible_sums.append(i)
            return possible_sums.__len__() == 4
