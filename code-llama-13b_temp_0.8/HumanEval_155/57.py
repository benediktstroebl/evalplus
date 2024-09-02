
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = str(num)[1:]
    else:
        num = str(num)

    return (sum(int(x)%2==0 for x in num), sum(int(x)%2==1 for x in num))
