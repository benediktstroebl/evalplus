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

# Test function to check if a given number is prime
def is_prime_test(n):
    return is_prime(n)

# Test array with values up to 200
test_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 213, 223, 227, 229, 233, 239, 241, 243, 247, 249, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 553, 559, 563, 569, 571, 577, 583, 587, 593, 601, 607, 613, 617, 619, 631, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 719, 731, 757, 763, 769, 787, 839, 857, 877, 881, 883, 897, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]

print("Test results:")")
for n in test_array:
    if is_prime_test(n):
        print(n, "is prime")
    else:
        print(n, "is not prime")
```
The function is_prime checks whether a given number is prime or not. It starts with a number is either less than or greater than 2. If so number is less than or equal to 3, it is prime. The function then checks if the number is divisible by 2 or 3. If it is, the number is not prime. If the number is not divisible by 2 or 3, the function checks if the square of the number is divisible by the number. If it is, the number is not prime. If the number is prime, the function returns True. If the number is not prime, the function returns False. 

The test function is_prime_test is used to check if a given number is prime or not. It simply calls the test the function is_prime with the given number. The test array is an array of numbers that are up to 200. The function then checks if the number is prime by calling the test function with the corresponding number.