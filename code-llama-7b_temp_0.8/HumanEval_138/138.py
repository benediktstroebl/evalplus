
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    else:
        n2 = n / 2
        n2s = int(n2)
        # print(n2)
        # print(n2s)
        for i in range(1,n2s+1):
            if n2 % i == 0:
                n3 = n2 / i
                n3s = int(n3)
                # print(n3)
                # print(n3s)
                for j in range(1,n3s+1):
                    if n3 % j == 0:
                        n4 = n3 / j
                        n4s = int(n4)
                        # print(n4)
                        # print(n4s)
                        for k in range(1,n4s+1):
                            if n4 % k == 0:
                                n5 = n4 / k
                                n5s = int(n5)
                                # print(n5)
                                # print(n5s)
                                if n5s == n:
                                    return True
    return False
