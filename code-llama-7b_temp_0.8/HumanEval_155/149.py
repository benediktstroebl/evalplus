
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def _helper(num, count):
        if num < 10:
            if num % 2 == 0:
                count[0] += 1
            else:
                count[1] += 1
        else:
            if num % 2 == 0:
                count[0] += 1
            else:
                count[1] += 1
            _helper(num // 10, count)
    count = [0, 0]
    _helper(num, count)
    return count

