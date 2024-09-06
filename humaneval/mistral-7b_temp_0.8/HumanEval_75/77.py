
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    print("I am is_multiply_prime function")
    a = int(input("Please enter a number: "))
    if a < 100:
        if a % 2 == 0:
            print(a," is a multiply of 2")
            if a % 3 == 0:
                print(a," is a multiply of 3")
                if a % 5 == 0:
                    print(a," is a multiply of 5")
                    print("The number is a multiply of 2,3 and 5")
                    return True
                else:
                    print("The number is not a multiply of 2,3 and 5")
                    return False
            else:
                print("The number is not a multiply of 2,3 and 5")
                return False
        else:
            print("The number is not a multiply of 2,3 and 5")
            return False
    else:
        print("The number is not less than 100")
        return False

