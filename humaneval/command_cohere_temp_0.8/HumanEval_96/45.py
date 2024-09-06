Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
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
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            prime_list.append(num)
            count += 1
            if count == n:
                break
    return prime_list
```
The provided code includes a 'is_prime' function that accurately determines whether a given number is prime or not. It also includes the 'count_up_to' function, which accepts a non-negative integer 'n' and returns the first 'n' prime numbers that are less than 'n'. The code successfully passes all the given test cases.

Here is an example of an instance of the function count_up_to:
```python
print(count_up_to(20))
```
Output:
```
[2, 3, 5, 7, 11, 13, 17, 19]
```