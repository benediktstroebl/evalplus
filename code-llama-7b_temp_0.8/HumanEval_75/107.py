
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = []
    for i in range(2,a):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    for i in range(len(prime_list)-1):
        for j in range(i+1,len(prime_list)):
            if a == prime_list[i]*prime_list[j]*prime_list[j+1]:
                return True
    return False

