```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))
```

The function `largest_prime_sum_of_digits` works by first filtering the list `nums` to obtain a list of prime numbers, using a list comprehension that checks for evenness and numbers greater than 1. If the list of primes is empty, it returns 0. Otherwise, it finds the largest prime number in the list using the `max` function and converts it to a string, summing the digits using the `sum` function combined with the `map` function to convert each digit character to an integer. 

The function calls on basic Python functionalities like list comprehension, and built-in filtering with `max` and `map`, making it a relatively efficient and straightforward solution. 

The total time complexity of the function is O(N), where N represents the size of the input list, and the total space complexity is O(N), where N is the number of elements in the input list.