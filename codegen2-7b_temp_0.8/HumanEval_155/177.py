
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    return (sum(n % 2 == 0 for n in str(num)), sum(n % 2!= 0 for n in str(num
