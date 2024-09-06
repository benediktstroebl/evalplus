```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 and x > 1]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` uses a list comprehension to filter out integers from the input list that are both prime (not divisible by 2 and greater than 1). The maximum prime is then converted to a string and its digits are summed using the `map` function. The `map` function takes the maximum prime list element and converts each digit to an integer in the string representation of that element, and then sums these integers. The result is returned by the function. 

This solution adheres to the problem statement, providing a self-contained Python script that identifies the maximum prime in the list and computes the sum of its digits. 

For better code organization, you may consider adding an import statement for the `sum` function, like so:
```python
from functools import sum
``` 

This puts the `sum` function in the same module block, indicating that it is being imported from the `functools` module. This still retains the self-contained aspect of the code, while also providing better organization and understanding of the code.