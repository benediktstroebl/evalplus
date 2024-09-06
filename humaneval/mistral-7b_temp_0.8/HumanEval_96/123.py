
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
    #make sure n is a non-negative number
    if n<0:
        print('n is negative')
    else:
        num=0
        prime_numbers=[]
        #while num<n
        while num<n:
            #check if num is prime, and if it is, append it to the list of prime numbers
            if is_prime(num):
                prime_numbers.append(num)
            #increment num by 1
            num+=1
        #return prime numbers
        return prime_numbers
    return 'oops, something went wrong'
