```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 and x != 1]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` takes a list of integers as input and returns the sum of the digits of the largest prime number in the list.

First, the function filters out all even numbers and singles (prime numbers) from the list using a list comprehension. It finds the largest prime number in the list using `max` and converts it to a string. Then, the function sums the digits of this string using `sum` and `map`. The `map` function converts each character of the string to an integer. 

The code efficiently solves the problem in a concise manner. You can test the function by providing different input lists in the console to see the result. 

For example, you can call the function like this:
```python
skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
```

The result will be:
```bash
10
```