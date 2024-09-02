
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num > 0:
        while num > 0:
            if num % 2 == 0:
                result = result * 10 + (num // 2)
            else:
                result = result * 10 + (num // 2) + 1
            num = num // 2
        return result
    else:
        return 0, 0

result, count = even_odd_count(num)
