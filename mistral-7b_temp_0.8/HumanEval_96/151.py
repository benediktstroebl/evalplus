
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    #Initialize an empty array to hold the prime numbers
    prime_list = []

    #Initialize a variable to hold the count
    count = 0

    #Initialize a variable to hold the current number being checked
    number = 2

    #While the count is less than the input number
    while count < n:

        #If the current number is not divisible by any other number (except itself and 1)
        if number != 0 and number != 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                #If the number is not divisible by any other number (except itself and 1)
                #Add it to the prime list
                prime_list.append(number)
                #Increase the count
                count += 1

        #Increase the number being checked
        number += 1

    #Return the prime list
    return prime_list
