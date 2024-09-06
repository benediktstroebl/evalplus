
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_num, odd_num = 0, 0
    for num in str(num):
        if num.isdigit():
            num = int(num)
            if num % 2 == 0:
                even_num += 1
            else:
                odd_num += 1
    return even_num, odd_
