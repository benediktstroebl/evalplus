```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function first filtering the list to only include prime integers, then finds the maximum sum of digits for the primes using a `max` and `sum` combination. This approach ensures that the list is efficiently reduced to only the primes, and the sum of digits is accurately computed for each prime number. 

To test this function, you can include a test list in the function call, like so:
```python
largest_prime_sum_of_digits([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])
``` 
This will return the value `10`, which is the expected output for the provided example list. 

Let me know if you have any questions or if you'd like to walk through any parts of the solution in greater depth!