
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
    result = []
    for x in range(n):
        is_prime = True
        for y in range(2, x):
            if x % y == 0:
                is_prime = False
                break
        if is_prime and x < n:
            result.append(x)
    return result




    Here we build a function that takes an input value and returns an array of the first n integers that are prime numbers and less than n.
    We loop through the range of all numbers from 2 up to the input value.
    For each number in the range, we loop through all numbers up to the number we are currently on.
    If the number is divisible by the number we are currently on, we know that number is not prime.
    We break out of the loop to prevent adding the number to the results array if it is not prime.
    If the number is prime and less than the input value, we append it to the results array.
    We return the array to the function.
