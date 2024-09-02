
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # YOUR CODE HERE
    if a<100:
        # print("a = ", a)
        if a%2!= 0:
            # print("a is odd")
            if a%3!= 0:
                # print("a is odd and not a multiple of 3")
                if a%5!= 0:
                    # print("a is odd and not a multiple of 3 and 5")
                    if a%7!= 0:
                        # print("a is odd and not a multiple of 3, 5 and 7")
                        return True
                    else:
                        # print("a is odd and not a multiple of 3, 5 and 7, but a multiple of 7")
                        return False
                else:
                    # print("a is odd and not a multiple of 3, 5 and 7, but a multiple of 5")
                    return False
            else:
                # print("a is odd and not a multiple of 3, 5 and 7, but a multiple of 3")
                return False
        else:
            # print("a is even")
            return False
    else:
        # print("a is bigger than 100")
        return False
