
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
    # Your code here
    # Replace pass with your code
    # if n <=0:
    #     return []
    # primes = [2]
    # curr_number = 3
    # while curr_number < n:
    #     # print(curr_number)
    #     divisor = 2
    #     while curr_number % divisor !=0 and divisor <= curr_number/2:
    #         # print('divisor is',divisor)
    #         divisor+=1
    #     if curr_number % divisor !=0:
    #         # print('curr is',curr_number)
    #         primes.append(curr_number)
    #     curr_number+=2
    # return primes
    primes = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes













































