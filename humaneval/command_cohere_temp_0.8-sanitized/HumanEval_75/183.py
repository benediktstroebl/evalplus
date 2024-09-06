def is_multiply_prime(a):
    # Write a Python program to check if a given number is a product of three prime numbers
    # Print true if the given number is the multiplication of 3 prime numbers 
    # and false otherwise
    if a < 100 and (a % 2 == 0 or a % 3 == 0 or a % 5 == 0):
        return True
    else:
        return False