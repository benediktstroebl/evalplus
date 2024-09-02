
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
    #loop through each number in range
    #check if each number is a prime number
    #append prime numbers to list
    #return list
    #FCC - Problem 1.2
    counter = 0
    numbers = []
    while counter < n:
        counter += 1
        is_prime = True
        for num in range(2, counter):
            if counter % num == 0:
                is_prime = False
        if is_prime:
            numbers.append(counter)
    return numbers
