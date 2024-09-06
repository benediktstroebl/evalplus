
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
    # initialize list of prime numbers
    prime_numbers = []
    # check for prime numbers less than n
    for num in range(2, n+1):
        # check if num is prime
        if num > 1:
            for i in range(2, int(num**0.5)):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    # reverse the order of the list
    return [prime_numbers[i] for i in range(len(prime_numbers))]

count_up_to_list = [list(count_up_to(n)) for n in range(1, 10)]
print(count_up_to_list)