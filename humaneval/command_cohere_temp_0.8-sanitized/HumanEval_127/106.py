def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def intersection(a, b):
    # Convert intervals to inclusive-inclusive format
    a = (a[0], b[1])
    b = (b[0], a[1])
    
    # Calculate the intersection length
    length = abs(min(a[1], b[1]) - max(a[0], b[0]))
    
    # Check if the length is prime
    if is_prime(length):
        return "YES"
    else:
        return "NO"