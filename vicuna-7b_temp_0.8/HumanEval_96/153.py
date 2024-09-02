
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
    # If n is 0, return an empty list
    if n == 0:
        return []
    
    # Check if n is prime
    if not is_prime(n):
        return []
    
    # Initialize the result list
    result = []
    
    # Recursively call the function with n-1
    result.extend(count_up_to(n-1))
    
    # Add the prime number up to n
    for i in range(2, int(n**0.5)+1):
        if is_prime(i):
            result.append(i)
            
    return result
