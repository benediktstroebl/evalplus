
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    i=2
    while i<=n:
        if n%i == 0:
            q=n/i
            if i==q:
                return False
            count=0
            while count<4:
                if i%2==0 and q%2==0:
                    count+=1
                i+=1
                q=n/i
                if q==i:
                    return False
            return True
        i+=2
    return False
