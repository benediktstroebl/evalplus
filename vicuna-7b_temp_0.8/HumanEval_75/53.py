
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a = int(input("Enter a number: "))
    if a < 1 or a > 100:
        print("Error: Number must be between 1 and 100.")
        return
    if a == 1:
        print("Error: Number can't be 1.")
        return
    for i in range(2, int(a**0.5) + 1):
        for j in range(i+1, int(a**0.5) + 1):
            for k in range(2, int(a**0.5) + 1):
                if a % i == 0 and a % j == 0 and a % k == 0:
                    print("Error: ", a, "is not a multiplication of 3 prime numbers.")
                    return
    print("Number", a, "is a multiplication of 3 prime numbers.")

a = int(input("Enter a number: "))
is_multiply_prime(a)