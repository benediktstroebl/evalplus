
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    #your code here
    


    #if len(string) == 1:
    #    return False

    #for i in range(2, len(string) // 2 + 1):
    #    if len(string) % i == 0:
    #        return False

    #return True

    #prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
    #p = 2
    #i = 0
    #while i < len(prime):
    #    if p == prime[i]:
    #        return True
    #    elif p > prime[i]:
    #        return False
    #    else:
    #        i += 1
    #        p += 1


    prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

    if len(string) in prime:
        return True
    else:
        return False

