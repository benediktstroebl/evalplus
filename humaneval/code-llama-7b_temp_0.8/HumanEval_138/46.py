
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    l = []
    for i in range(2,n):
        for j in range(2,i):
            if (i+j)%2==0 and (i+j)<n:
                l.append(i+j)
            if l==[4,6,10,12]:
                return True
    return False

