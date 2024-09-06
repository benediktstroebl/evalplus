
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
    # Set a variable for the current number to check
    num = n
    # Iterate through the prime numbers up to sqrt(n)
    for num in range(2, int(n**0.5) + 1):
        # If num is prime and less than n, append it to the list
        if num > 1 and num % 2 != 0 and num % 3 != 0 and num % 4 != 0 and \
           num % 6 != 0 and num % 7 != 0:
            yield num
        # If num is greater than n, stop checking
        else:
            break
