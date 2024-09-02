
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = sum(i for i in str(num) if i.isdigit() and int(i) % 2 == 0)
    odd = sum(i for i in str(num) if i.isdigit() and int(i) % 2!= 0)
    return (even, odd
