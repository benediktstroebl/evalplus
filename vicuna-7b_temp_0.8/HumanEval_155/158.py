
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digit_list = str(num).split('.')
    if len(digit_list) == 1:
        return 0, 0
    else:
        odd_count = 0
        for i in range(len(digit_list)):
            if digit_list[i] % 2 != 0:
                odd_count += 1
        return int(odd_count), int(len(digit_list) - odd_count)
