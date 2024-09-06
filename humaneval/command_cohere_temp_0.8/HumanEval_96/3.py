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
    numbers = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            numbers += [i]
            count += 1
            if count == n:
                break
    return numbers
```
The `count_up_to()` function takes an integer `n` as an argument and creates an array of the first `n` integers that are prime numbers less than `n`. The `is_prime()` function is used to check if a number is prime. The overall time complexity of the program is O(N * log(N)) where N is the value of n passed to count_up_to(), this is because we check each element in range(2, n+1) if it is prime and checking if a number is prime takes O(log(N)) time.

Here is an example of an invocation of this script:
```python
print(count_up_to(20))
```
This will print:
```
[2, 3, 5, 7, 11, 13, 17, 19]
```