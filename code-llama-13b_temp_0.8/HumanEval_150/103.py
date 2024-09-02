
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # your code here
    # if n is prime, return x
    # otherwise, return y

    # check if n is a prime
    # if it is a prime number, then return x
    # otherwise return y
    
    #create a variable that checks for prime numbers
    #start with 2 which is the smallest prime number
    #if n is divisible by 2, then it is not a prime number
    #if it is divisible by itself, it is also not a prime number
    #if it is divisible by any number in between 2 and n - 1, it is also not a prime number
    #if none of the above, then it is a prime number
    #only check up to the square root of a number

    for i in range (2, n):
        if n % i == 0:
            #not a prime number
            return y
            break
        #if the number is not divisible by any number between 2 and n - 1, then it is a prime number
        else:
            #prime number
            return x
            break

    # print(x_or_y(7, 34, 12)) # Should return 34
    # print(x_or_y(15, 8, 5)) # Should return 5
    return x
