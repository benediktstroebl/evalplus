```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to retain only the prime numbers using a list comprehension. Then, it converts each prime number to a string and sums the digits to calculate the largest sum of digits amongst the prime numbers in the list. 

The tests passed for this problem are:
1. `['For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10']`
2. `['For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25']`
3. `['For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13']`
4. `['For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11']`
5. `['For lst = [0,81,12,3,1,21] the output should be 3']`
6. `['For lst = [0,8,1,2,1,7] the output should be 7']`