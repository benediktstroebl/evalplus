
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def_even = 0
    def_odd = 0
    for i in num:
        if i % 2 == 0:
            def_even += 1
        else:
            def_odd += 1
    return(def_even, def_odd)
