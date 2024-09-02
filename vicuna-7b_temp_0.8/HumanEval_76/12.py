
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # TODO: Write the code for the function is_simple_power(x, n).
    # You should use a loop to check all prime factors of n.
    # If n is prime, check if x is equal to n**int for some int.
    # If n is not prime, check if there exists a prime factor of n that divides x.
    # Return the result of your function.
    # Print the result.

x = 12
n = 13
result = is_simple_power(x, n)
