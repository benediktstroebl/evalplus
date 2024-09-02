
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n==0:
        return True
    if n<4 or n%2==1:
        return False
    num=0
    for i in range(0,int(n/2)+1):
        if i*2<=n-i*2:
            num+=1
    if num>=4:
        return True
    else:
        return False

















































