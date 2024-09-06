
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    convert_num_to_list = list(str(num))
    even = 0
    odd = 0
    for num in convert_num_to_list:
        if int(num) % 2 == 0:
            even += 1
        else:
            odd += 1

    list_to_tuple = (even, odd)
    return list_to_tuple

