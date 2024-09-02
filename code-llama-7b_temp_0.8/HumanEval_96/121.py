
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
    #First we need to create an empty list
    arr = []

    #Then, we need to create a loop that runs 
    #the length of n
    for i in range(n):

        #Then, we need to create a loop that
        #checks if the number is a prime number 
        for j in range(2, i+1):

            #If it is not prime, we want to break out of the loop
            if i % j == 0 and i != j:
                break

            #If it is prime, we want to append it to the array
            else:
                arr.append(i)

    #Finally, we return the array
    return arr
