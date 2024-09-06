```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to retain only prime numbers, using a list comprehension that checks for evenness and numbers greater than 1. It then finds the maximum sum of digits across all prime numbers using a generator expression within the max function, which iterates through the prime numbers and converts each one to a string, summing the digits. 

The `primes` list comprehension is used to filter out non-prime, non-positive numbers from the list, leaving only the largest prime numbers to be processed by the max and sum operations. 

Please note that this approach assumes that the list `lst` contains only positive integers. If the list could potentially contain non-positive values, additional preprocessing would be necessary to handle those cases. 

This solution has an time complexity of O(n*log(log(n))) as it iterates through the list once and then iterates through the prime numbers within the max and sum operations, with an input length logarithmic complexity. 

This solution should work correctly for the given problem statements. Let me know if you'd like me to explain any part of the solution or provide further clarifications!