```python
def is_prime(n):
    """Check if a number is prime."""
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

# Test function to check if a number is prime
def is_prime_test(n):
    return is_prime(n)

# Test array with numbers to check for prime
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 213, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 321, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 419, 421, 443, 449, 457, 461, 463, 467, 479, 487, 493, 499, 503, 509, 521, 523, 539, 541, 547, 553, 559, 563, 569, 571, 577, 587, 593, 601, 613, 617, 619, 631, 643, 659, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 751, 757, 763, 769, 787, 797, 809, 821, 829, 859, 863, 877, 881, 883, 887, 891, 917, 923, 937, 961, 969, 987, 991, 997, 1009]

# Check if all numbers are prime
all_ prime = all(is_prime_test(n) for n in numbers)
print("All numbers are prime:", all_ prime)
``` 
This Python code defines a function `is_prime` that checks whether a given number is prime or not. It then tests a both the and checks for various cases for primality, such as even and odd numbers, and numbers divisible by 2 and 3. Finally, it tests an set of numbers against the `is_prime` function and prints the result.