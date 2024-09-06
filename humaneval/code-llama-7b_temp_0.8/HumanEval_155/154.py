
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    #return len([i for i in str(num) if int(i) % 2 == 0]), len([i for i in str(num) if int(i) % 2 != 0])
    odd = []
    even = []
    for i in str(num):
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
    return len(even), len(odd)
