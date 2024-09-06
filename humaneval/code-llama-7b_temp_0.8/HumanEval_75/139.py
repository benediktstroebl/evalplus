
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # TODO: Write your solution here
    number=str(a)
    if len(number)==1:
        if a%2==0 or a%3==0:
            return False
        else:
            return True
    prime=[]
    for i in range(2,a):
        if a%i==0:
            if is_prime(i)==True:
                prime.append(i)
        if len(prime)==3:
            break
    if len(prime)==3:
        if number==str(prime[0]*prime[1]*prime[2]):
            return True
        else:
            return False
    else:
        return False

