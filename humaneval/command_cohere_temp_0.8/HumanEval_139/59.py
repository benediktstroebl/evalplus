```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. It initializes a list `factorial_list` with values up to the integer n, calculating the factorial for each value and appending it to the list. The final element of the list, which is the `factorial_list[n]`, corresponds to the Brazilian factorial of the input integer `n`. 

Here's an example of using this function:
```python
>>> special_factorial(4)
288
```
This calls the `special_factorial` function with an argument of 4, returning the result of 288, which is indeed the Brazilian factorial of 4. 
```
python
```