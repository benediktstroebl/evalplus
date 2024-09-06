

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    # If the number is prime then return its digits
    # else return the digit sum of its largest prime factor
    # Loop through all numbers in the list, starting at 2
    # If the number is prime, check the next number, if not
    # check its prime factors and return the sum of the largest
    # prime factor
    # If not return 0

    # Hint: Use a loop and if/else

    # get the largest prime
    # if the number is prime get the sum of its digits
    # else get the largest prime factor and get the sum of its digits

    # start at 2
    # if the number is prime, continue
    # if the number is not prime, check the next number
    # if it is prime, check the next number
    # if it is not prime, check the largest prime factor
    # if the largest prime factor is prime, check the next number
    # if it is not prime, check the largest prime factor

    #1931014981
    # 1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3

    for num in lst:
        isPrime = False
        if num < 2:
            continue
        if num == 2:
            return sum([int(n) for n in str(2)])

        for i in range(2, num+1):
            if num % i == 0:
                # is it prime?
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    isPrime = True
                    break

        if isPrime:
            return sum([int(n) for n in str(num)])

        largest = 1
        for i in range(2, num+1):
            if num % i == 0:
                # is it prime?
                for j in range(2, i):
                    if i % j == 0:
