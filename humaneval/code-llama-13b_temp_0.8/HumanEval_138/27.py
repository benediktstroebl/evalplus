
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 == 0:
        return False
    else:
        cnt = 0
        s = 0
        for i in range(1,int(n/2)+1):
            if n%i == 0:
                cnt += 1
                s += i
                if s == n:
                    if cnt == 4:
                        return True
                    else:
                        return False
                elif s > n:
                    break
                else:
                    continue
            else:
                continue
    return False
        
