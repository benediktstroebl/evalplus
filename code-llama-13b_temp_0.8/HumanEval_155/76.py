
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    def count_even_odd(n):
        count = [0, 0]
        while n:
            count[n % 2] += 1
            n //= 10
        return tuple(count)
    if num < 0:
        num = -num
    return count_even_odd(num)
