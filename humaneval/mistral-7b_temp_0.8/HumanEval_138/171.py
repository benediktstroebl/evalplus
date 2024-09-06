
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """


    a = []

    while n%2 == 0:
        a.append(2)
        n = n//2

    if n%2 == 1:
        return False

    b = []
    for i in range(4,n,2):
        b.append(i)
    for i in range(2,n,2):
        b.append(i)
    for i in b:
        if i in a:
            b.remove(i)

    if len(b) != 4:
        return False

    if sum(b) == n:
        return True
    return False
