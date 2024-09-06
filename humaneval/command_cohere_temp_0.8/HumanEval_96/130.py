Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    prime_list = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            prime_list.append(i)
            count += 1
            if count == n:
                break
    return prime_list

# Example usage
n = int(input("Enter a number: "))
print(count_up_to(n))
```
This script defines a function `count_up_to(n)` that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n. The function checks each number recursively to see if it is prime, starting from 2 and incrementing by 1 until the desired number of primes has been collected or the limit n has been exceeded. 

Here is an example of how to use this function:
```python
n = int(input("Enter a number: "))
print(count_up_to(n))
```
This will take a number from the user and print the first n prime numbers less than n.