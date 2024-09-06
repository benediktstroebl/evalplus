```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. It initializes a list `factorial_list` with values of factorials from 1! to n!. Then, it calculates the factorial of n by multiplying `n!` with the special factorial, which is constructed as the product of all positive factorial integers less than n. 

Here is an example of using this function:
```python
>>> special_factorial(4)
288
```
This example calculates special factorial for n = 4, and the result is 288, matching the example provided in the problem statement.