
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    return (len(str(num)), len([i for i in str(num) if i == '1' or i == '3' or i == '5' or i == '7' or i == '9']))
