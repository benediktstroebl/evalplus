
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    return (len(re.findall(r'(\d)[^\d]', str(abs(num)))), len(re.findall(r'[^02468][\d]', str(abs(num)))))

