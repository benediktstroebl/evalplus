
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (1, 0)
    if num < 0:
        return even_odd_count(-num)
    if num % 2 == 0:
        return (even_odd_count(num//10)[0] + 1, even_odd_count(num//10)[1])
    else:
        return (even_odd_count(num//10)[0], even_odd_count(num//10)[1] + 1)
