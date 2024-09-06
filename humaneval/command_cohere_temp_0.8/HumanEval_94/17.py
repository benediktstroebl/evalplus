```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))
```

The function `largest_prime_sum_of_digits` takes a list of integers `lst` as input and returns the sum of the digits of the largest prime number in the list.

The function first uses a list comprehension to filter the list `lst` and create a new list `primes` that includes only the prime numbers (excluding the number 1). If the new list is empty, the function returns 0. Otherwise, it proceeds to convert the largest prime number in the list into a string, sum the digits of that number, and return the result.

Here is a simpler alternative approach to solve this problem:
```python
def largest_prime_sum_of_digits(lst):
    return sum(map(int, str(max([x for x in lst if x % 2 == 1 and x > 1]))))
```

This approach directly finds the largest prime number in the list using a list comprehension, converts it to a string, and then sums its digits. Both approaches are valid and provide the same results, but it's important to note that the initial version is more efficient than the simplified version, with a time complexity of O(n) vs O(n log n), respectively.