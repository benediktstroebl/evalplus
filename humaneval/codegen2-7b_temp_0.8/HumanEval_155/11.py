
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = sum(1 for num in str(num) if num.isdigit())
    odd_count = sum(1 for num in str(num) if num.isdigit() and num % 2 == 1)
    return (even_count, odd_count
