
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num > 0:
        num = str(num)
        odd_count = 0
        for i in range(len(num)):
            if num[i] == '1':
                odd_count += 1
            elif num[i] == '0':
                odd_count += 1
        even_count = len(str(num)) - odd_count
        return odd_count, even_count
    else:
        return 0, 0
