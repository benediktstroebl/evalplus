
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Your code here
    # return (len([x for x in str(num) if x.isdigit() and int(x) % 2 == 0]),
    #         len([x for x in str(num) if x.isdigit() and int(x) % 2 == 1]))
    count = (0, 0)
    for x in str(num):
        if x.isdigit():
            if int(x) % 2 == 0:
                count[0] += 1
            elif int(x) % 2 == 1:
                count[1] += 1
    return count
