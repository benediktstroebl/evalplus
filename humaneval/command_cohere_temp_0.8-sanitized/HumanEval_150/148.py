def is_prime(n):
    """ Checks if a number is prime """
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def x_or_y(n, x, y):
    """ Returns x if n is a prime number, otherwise returns y """
    if is_prime(n):
        return x
    else:
        return y
n = int(input("Enter a number: "))
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))