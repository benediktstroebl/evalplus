
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # your code here
    even = 0
    odd = 0
    count = 0
    if(num<0):
        num = abs(num)
    while(num>0):
        count = num%10
        num = num//10
        if(count%2==0):
            even+=1
        else:
            odd+=1
    return (even,odd)

