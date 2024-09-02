
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_string = str(abs(num))
    even_count = sum([1 for x in num_string if x in "02468"])
    odd_count = len(num_string) - even_count
    return even_count, odd_count

