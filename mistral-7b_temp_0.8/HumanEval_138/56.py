
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Add your code here
    count=0
    for i in range(1,n//2+1):
        for j in range(i+1,n//2+1):
            for k in range(j+1,n//2+1):
                for l in range(k+1,n//2+1):
                    if (i+j+k+l)==n:
                        count+=1
                        break
                if count==1:
                    break
    if count==1:
        return True
    else:
        return False
