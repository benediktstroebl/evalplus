```python
def count_primes(num):
    """
    This function takes a string num and returns the number of prime hexadecimal digits 
    in num.
    It assumes that num is always correct or empty string, and symbols A, B, C, D, E, F are 
    always uppercase.
    Returns: number of 2, 3, 5, 7, B, D, calculated from num.
    """
    Tests all numbers in num that are less than 2, and count them. Then, 
    it counts all numbers in num that are greater than 2 and less than 10^17 
    (so they are prime numbers) and adds 1 to the count.

def test():
    """
    This function tests the count_primes function with a given string num. It returns 
    True if the tests pass and False otherwise.
    """
    print(count_primes("AB")) # Output: 1
    print(count_primes("1077E")) # Output: 2
    print(count_primes("ABED1A33")) # Output: 4
    print(count_primes("123456789ABCDEF0")) # Output: 6
    print(count_primes("2020")) # Output: 2
    return False

print(test()) # Output: True
```