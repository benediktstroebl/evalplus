
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
    # initialize prime_numbers to an empty array
    prime_numbers = []
    # initialize counter to 0
    counter = 0
    # create a for loop to iterate through integers from 2 to n
    for num in range(2, n+1):
        # create a boolean variable called is_prime to keep track of whether a number is prime
        is_prime = True
        # create a for loop to iterate through each integer in prime_numbers
        for i in prime_numbers:
            # check if the current number is divisible by the current prime number
            if num % i == 0:
                # if it is divisible, set is_prime to false
                is_prime = False
                # break out of the inner for loop
                break
        # if is_prime is true, add the current number to prime_numbers
        if is_prime:
            prime_numbers.append(num)
        # increment the counter by 1
        counter += 1
    # return prime_numbers
    return prime_numbers
