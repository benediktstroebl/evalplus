
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
    # Use a list to store the primes
    primes = []
    # Use a variable to track the number of primes
    count = 0
    
    # Check for and handle the special case of n=0
    if n == 0:
        return []
    
    # Check for and handle the special case of n==1
    if n == 1:
        return []
    
    # Use a for loop to check for and include all the numbers less than n in the primes list
    for num in range(2, int(n**0.5)+1):
        if num > 1:
            # Use the divisor_check function to check if num is divisible by any of the primes in the primes list
            is_divisible = check_divisibility(num, primes)
            
            # If num is not divisible by any of the primes in the primes list, add it to the primes list
            if not is_divisible:
                primes.append(num)
            
            # Increment the count variable
            count += 1
    
    # Return the count variable as the array of primes
    return count
