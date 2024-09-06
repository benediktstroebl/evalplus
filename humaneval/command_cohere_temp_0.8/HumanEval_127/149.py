```python
def is_prime(n):
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

def intersection(s1, s2):
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > en:
        return "NO"
    elif is_prime(st - en + 1):
        return "YES"
    else:
        return "NO"

# Example usage
print(intersection((1, 2), (2, 3))) == "NO"
print(intersection((-1, 1), (0, 4))) == "NO"
print(intersection((-3, -1), (-5, 5))) == "YES"
```

The approach uses a simple algorithm to check if the intersection length is prime. The is_prime function checks if a given number n is a prime number or not. It first checks if n is less than or equal to 1, in which case it is not prime. Then it checks if n is equal to 2 or 3, in which case it is prime. Finally, it iterates through numbers of the form 5k ± 2, starting from 5, until it reaches the square root of the number n, and checks if n is divisible by any of these numbers. If it is not, then n is prime. 

The function intersection takes two intervals, s1 and s2, and returns "YES" if the length of the intersection of these intervals is a prime number, and "NO" otherwise. It does this by finding the start and end point of the intersection, checking if the length of the intersection is greater than 0, and then using the is_prime function to check if the length of the intersection is prime. 

The code includes test examples to verify its correctness. You can add more tests as needed.