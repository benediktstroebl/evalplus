
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # your code here
    count = 0
    evencount = 0
    for i in num:
        if i%2==0:
            evencount+=1
        else:
            count+=1
    return evencount,count
