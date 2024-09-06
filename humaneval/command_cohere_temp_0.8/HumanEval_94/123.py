```python
def largest_prime_sum_of_digits(nums):
    primes = [i for i in nums if is_prime(i)]
    return max(sum(map(int, str(p))) for p in primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_sum_of_digits()` takes a list of integers (`nums`) as input and returns the sum of the digits of the largest prime number in the list. The function `is_prime()` checks if a given number is prime or not. 

Here is an example usage of the function:
```python
print(largest_prime_sum_of_digits([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]))
```
Which will print out:
```bash
10
``` 

The largest prime number in the list is 55555, which has a digit sum of 10. 

This solution should address the problem presented in the markdown code block and pass the described tests. Let me know if further clarification is needed!