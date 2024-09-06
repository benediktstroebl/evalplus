```python
def skjkasdkd(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return sum(map(int, str(max(primes, key = lambda x: x))))
```

The function `skjkasdkd` takes a list of integers as input and first filters the list to only include prime numbers using a list comprehension. Then, it finds the maximum prime value using the `max` function with a custom key to compare integers by their numerical value. Finally, it converts the maximum prime value to a string and sums up the digits using the `map` function and the `int` function. The `all` function is used with a generator expression to check if a number is prime or not. 

Here is an example usage of the function:
```python
print(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]))
```

This would print out:
```
10
```