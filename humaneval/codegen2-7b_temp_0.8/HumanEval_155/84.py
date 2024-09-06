
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(num)
    even = 0
    odd = 0
    for i in range(len(num_str)):
        if num_str[i].isdigit():
            if int(num_str[i]) % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even,
