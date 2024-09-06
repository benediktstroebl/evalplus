
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n2 = n
    n3 = n
    n4 = n
    # write your code here
    #n = int(input("Enter a number: "))
    #if n == 4 or n == 6 or n == 8:
     #   return False
    #else:
     #   return True
    while n != 8:
        if n%2 == 0:
            n = n + n2
            n2 = n2 + n3
            n3 = n3 + n4
            n4 = n4 + n
            #n = n + n2
            #n2 = n2 + n3
            #n3 = n3 + n4
            #n4 = n4 + n
        else:
            return False
    return True

