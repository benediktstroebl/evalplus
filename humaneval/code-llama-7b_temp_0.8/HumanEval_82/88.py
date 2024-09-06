
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check if the string length is a prime number
    # how do we know if it is prime?
    # a number is prime if it cannot be divided by any other number
    # except for 1 and itself
    # we'll have to count the number of "divisors" and if it is 2, then
    # it is a prime
    # to count the number of divisors, we can loop through every digit
    # of the number and check if it divides the string length without
    # a remainder
    # but how do we check if it divides without a remainder?
    # how about we divide the string length by the number and check if
    # the result is an integer?
    divisors = 0
    for i in range(2, string.__len__()):
        if string.__len__() % i == 0:
            divisors += 1
    # if the number of divisors is 2, then the string length is prime
    # otherwise, it is not
    return True if divisors == 2 else False
