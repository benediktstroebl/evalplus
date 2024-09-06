def count_up_to(n):
    # Iterate through numbers from 2 to n-1
    for num in range(2, n):
        # Check if the number is prime
        if is_prime(num):
            # Append the prime number to the result list
            yield num 
    return
def is_prime(num):
    # Check if the number is 1 or less than 1, which makes it not prime
    if num < 2:
        return False 
    # Check if the number is even and divisibly by 2, which makes it not prime
    if num % 2 == 0:
        return False 
    # Check divisibility by 3, which makes it not prime
    if num % 3 == 0:
        return False 
    # Check divisibility by 5, which makes it not prime
    if num % 5 == 0:
        return False 
    # Check divisibility by 7, which makes it not prime
    if num % 7 == 0:
        return False 
    # Check divisibility by 11, which makes it not prime
    if num % 11 == 0:
        return False 
    # Check divisibility by 13, which makes it not prime
    if num % 13 == 0:
        return False 
    # If the number is not divisible by 2, 3, 5, 7, 11, 13, it is prime
    return True