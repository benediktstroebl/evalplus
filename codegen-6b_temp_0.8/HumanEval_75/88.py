
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def number_to_list(n):
        l = [int(i) for i in str(n)]
        return l

    def list_to_number(l):
        return int("".join([str(i) for i in l]))

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        for i in range(2, n):
            if not n % i:
                return False
        return True

    def is_3_divisible(n):
        if n % 3 == 0:
            return True
        else:
            return False


    a = number_to_list(a)
    a = [i for i in a if is_prime(i)]
    l = len(a)
    for i in range(1, l):
        if not is_prime(list_to_number(a[:i]) * list_to_number(a[i:])):
            return False
    return True


