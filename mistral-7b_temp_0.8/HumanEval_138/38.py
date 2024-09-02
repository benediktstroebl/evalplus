
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # number of numbers to be summed
    count = 4
    # array to store sum of numbers
    sum_num = []
    # flag to track solution
    found = False
    # loop to check all possible combinations
    for i in range(count):
        for j in range(i+1, count):
            for k in range(j+1, count):
                for l in range(k+1, count):
                    if (i+j+k+l == n):
                        for number in (i, j, k, l):
                            if (number % 2 != 0):
                                return False
                        sum_num = [i, j, k, l]
                        found = True
    if (found == True):
        return sum_num
    return False
