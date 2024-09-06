
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
    # This returns the next prime number after the number passed as a parameter
    def next_prime(number):
        if number % 2 == 0:
            return number + 1
        for i in range(3, int(number**0.5), 2):
            if number % i == 0:
                return next_prime(number+1)
        return number

    prime_numbers = []
    for i in range(2, n):
        if i % 2 == 0 and i != 2:
            continue
        prime_numbers.append(i)
        if i == n:
            return prime_numbers
        i = next_prime(i)
    return prime_numbers
