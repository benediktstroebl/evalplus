
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even,odd = 0,0
    for x in range(0,len(str(num)),1):
        if int(str(num)[x])%2 == 0:
            even += 1
        else:
            odd += 1
    return (even,odd)

