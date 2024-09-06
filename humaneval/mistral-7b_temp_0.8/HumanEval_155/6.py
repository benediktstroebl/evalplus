
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(num)
    num_str_list = [int(i) for i in num_str]
    num_str_list_even = list(filter(lambda x: x%2==0, num_str_list))
    num_str_list_odd = list(filter(lambda x: x%2!=0, num_str_list))
    return (len(num_str_list_even), len(num_str_list_odd))

