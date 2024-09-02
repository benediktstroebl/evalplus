
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Your code here
    count_e = 0
    count_o = 0
    temp_num = num
    while temp_num > 0:
        last_digit = temp_num%10
        if last_digit % 2 == 0:
            count_e += 1
        else:
            count_o += 1
        temp_num = temp_num//10
    return (count_e,count_o)
