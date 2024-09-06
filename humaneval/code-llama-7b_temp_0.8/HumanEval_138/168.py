
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    e = []
    for i in range(2,n):
        if i%2==0:
            e.append(i)
    for i in range(0,len(e)):
        for j in range(i+1,len(e)):
            for k in range(j+1,len(e)):
                for l in range(k+1,len(e)):
                    if e[i]+e[j]+e[k]+e[l]==n:
                        return True
    return False

