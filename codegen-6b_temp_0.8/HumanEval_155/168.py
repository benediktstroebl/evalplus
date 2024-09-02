
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    
    num_str = str(abs(num))
    
    len_even = 0
    len_odd = 0

    for i in range(0, len(num_str)):
        if i % 2 == 0 and int(num_str[i]) % 2 == 0:
            len_even += 1

        elif i % 2 != 0 and int(num_str[i]) % 2 != 0:
            len_odd += 1

    return len_even, len_odd