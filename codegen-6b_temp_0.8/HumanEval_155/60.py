
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    import operator
    def num_to_str(num):
        if int(num) < 10:
            return str(num)
        else:
            return num_to_str(int(num/10)) + str(num%10)
    if num < 0:
        num = abs(num)
    n = num_to_str(num)
    return (n.count('0'), n.count('1'))
