
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num > 0:
        str_num = str(abs(num))
        even_digits = 0
        odd_digits = 0
        for i in range(len(str_num)):
            if int(str_num[i]) % 2 == 0:
                even_digits += 1
            else:
                odd_digits += 1
        return even_digits, odd_digits
    elif num < 0:
        str_num = str(abs(num))
        even_digits = 0
        odd_digits = 0
        for i in range(len(str_num)):
            if int(str_num[i]) % 2 == 0:
                odd_digits += 1
            else:
                even_digits += 1
        return even_digits, odd_digits
    else:
        return 1, 1

