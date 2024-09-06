```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers as input and returns the sum of the digits of the largest prime number in the list.

The list is first filtered to include only the elements greater than 1 and the primes with digits exceeding the range from 3 to the square root of the number. The `map` function is then used to convert the prime numbers to strings and back to integers to calculate their digit sums. Finally, the maximum digit sum of the prime is returned. 

This approach ensures that the code efficiently finds the correct largest prime number and calculates its digit sum. 
Here is an example of an input and an output:
```
input_lst = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]
print(largest_prime_sum_of_digits(input_lst))  # output: 10
```