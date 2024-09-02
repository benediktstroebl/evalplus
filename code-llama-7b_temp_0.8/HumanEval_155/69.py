
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    return len([n for n in str(num) if int(n)%2==0]), len([n for n in str(num) if int(n)%2==1])
    
    # return str(num).count('0'),str(num).count('1')
