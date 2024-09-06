
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    #declare a variable to store the integers in order
    ints = []
    #for every number between a and b,
    for num in range(a, b + 1):
        #split the number into a list of its digits
        list_of_digits = list(str(num))
        #if the number has an even number of digits,
        if len(list_of_digits) % 2 == 0:
            #and if the number has an even digit at an even index,
            if int(list_of_digits[0]) % 2 == 0:
                #add the number to the list of integers
                ints.append(num)
    #return the list of integers
    return ints
