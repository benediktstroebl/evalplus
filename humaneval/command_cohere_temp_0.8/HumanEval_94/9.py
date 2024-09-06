```python
def skjkasdkd(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` takes a list of integers as input and first filters out all prime numbers from the list using a list comprehension. Then, it finds the maximum prime number and converts it to a string, summing up the digits of that string to return as the output.

To run this code properly, you would need to install the Python package "itertools" since the code is using the `filter` function from it. If it is not already installed, you would need to run the following command:
```
pip install itertools
``` 

The code should work correctly after installation or if it is already installed on your system.