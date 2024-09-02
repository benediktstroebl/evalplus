
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Open a file to read and write the input
    with open("input.txt", "r") as f:
        # Read the number from the file
        number = int(f.readline())
        # Close the file
        f.close()
        # print number
        return number % 2 != 0 or number % 3 == 0 or number % 5 == 0
