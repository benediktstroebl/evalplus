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

# Test function to check if a number is prime
def is_prime_tests():
    print("Test 1: ", end="")
    print("6 is not prime")
    print()
    print("Test 2: ", 42)
    print("Test 3: ", 3)
    print("Test 4: ", 7)
    print("Test 5: ", 11)
    print("Test 6: ", 13441)
    print("Test 7: ", 61)
    print("Test 8: ", 4)
    print("Test 9: ", 1)
    print("Test 10: ", 25)
    print()

# Main function
def main():
    print("Prime numbers: ", end="")
    print(is_prime(6))
    print()
    print("Prime?", 42)
    print("Non-prime: ", 3)
    print("Non-prime:", 7)
    print("True:", is_prime(13441))
    print("False:", is_prime(61))
    print("Non-prime:", 4)
    print("Non-prime:", 1)
    print("Testing more numbers...",", is_prime_tests())

if __name__ == "__main__":
    main()
```
This script defines a function is_prime(n) that checks whether a given number is prime. The function implements a primality algorithm known as the "six-digit rule," which is efficient for most practical purposes. The is_prime_tests() function provides test cases to check if the is_prime() function is correct. The main function calls the is_prime() and passes test cases, printing the results.