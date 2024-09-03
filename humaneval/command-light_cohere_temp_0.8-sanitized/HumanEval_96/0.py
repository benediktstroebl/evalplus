def count_up_to(n):
    """Return array of prime numbers less than or equal to n."""
    lis = [2] 
    for i in range(3, n+1): 
        if is_prime(i) == True: 
            lis.append(i) 
    return lis
def is_prime(n):
    """Check if n is prime."""
    if n <= 1: 
        return False
    if n <= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i += 6
    return True
n = int(input("Enter n: "))