def is_multiply_prime(a):
    # check if a is less than 100
    if a < 100:
        # check if the root of a is an integer
        if int(root(a)) == a: 
            # check if a is the multiplication of 3 prime numbers
            return True
    return False
def root(a):
    return int(input("Enter the root of %s: " % a))