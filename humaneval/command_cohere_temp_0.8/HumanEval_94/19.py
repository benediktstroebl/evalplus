```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 and x != 1]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` uses a list comprehension to filter out non-prime and even numbers from the list, and then finds the maximum prime number using max. The digits of this maximum prime are then converted into an integer sum using `map`, and returned. 

This should be added to a markdown code block with the following header:
```python
```

This code block should then be placed within a ````python
```

This will ensure the code block is interpreted as Python code, allowing users to run it as is.