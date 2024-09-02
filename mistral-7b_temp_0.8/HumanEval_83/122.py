
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    #first figure out how many 1's there are
    #then figure out how many digits there are
    #then multiply those two together
    #this will give us the number of one digit integers
    #first figure out how many n digit integers that start or end with 1
    #last figure out how many n digit integers there are
    #then divide the last number by the first number
    #this will give us the percentage
    #first figure out how many one digit integers there are
    #last figure out how many n digit integers there are
    #then divide the last number by the first number
    #this will give us the percentage
    #for n digits there are 10^n
    #for one digit there are 10
    #so divide them
    print(10 ** n / 10)

