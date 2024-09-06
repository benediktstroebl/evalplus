```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to obtain a list of prime integers (`primes`). Then, it calculates the sum of the digits of each prime number and selects the largest sum among them using the `max` function. The `map(int, str(x))` expression converts the prime number `x` to a string and then converts each character of the string back to an integer, effectively converting each prime number to a decimal representation and summing its digits. 

Overall, the code efficiently solves the problem statement and returns the desired output. You can test it by providing different input lists in the `lst` parameter.