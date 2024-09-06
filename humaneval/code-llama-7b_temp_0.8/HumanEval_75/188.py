
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if(a < 100):
        prime1 = 0
        prime2 = 0
        prime3 = 0
        count1 = 0
        count2 = 0
        count3 = 0

        #Looping all numbers between 1 and a
        for i in range(1,a):
            #Check if i is prime
            if(is_prime(i) == True):
                #Check if i is multiply of prime1
                if(prime1 == 0 or prime1*i == a):
                    count1+=1
                    prime1 = i
                #Check if i is multiply of prime2
                elif(prime2 == 0 or prime2*i == a):
                    count2+=1
                    prime2 = i
                #Check if i is multiply of prime3
                elif(prime3 == 0 or prime3*i == a):
                    count3+=1
                    prime3 = i
                
        if(count1 == 1 and count2 == 1 and count3 == 1):
            return True
        else:
            return False
