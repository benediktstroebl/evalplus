
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

    # Create an array to save the prime numbers
    prime_numbers = []

    # Create a for loop that counts from 2 to n
    for num in range(2, n + 1):
        is_prime = True
        # Create a for loop that counts from 2 to num-1
        for i in range(2, num):
            # If the remainder of num divided by i is 0, set is_prime to false
            if num % i == 0:
                is_prime = False
                # If is_prime is false, don't append the number to prime_numbers
                break
        # If is_prime is true, append the number to prime_numbers
        if is_prime:
            prime_numbers.append(num)

    # Return the prime_numbers array
    return prime_numbers
