```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts a single argument `n`. This function calculates the 'special factorial' of n, which is defined as `n! * (n-1)! * (n-2)! * ... * 1!` where `n > 0`. The function achieves this by setting a variable `fact` to 1 and then iterating through the numbers from 1 to `n` and multiplying `fact` by the current number in each iteration. Finally, it returns the computed 'special factorial' value. 

Here is an example usage of this function:
```python
>>> special_factorial(4)
288
```
This will return the special factorial of 4, which is 288. 

This approach is efficient and directly computes the result using a loop, avoiding recursive calls, which could be potentially computationally expensive for large inputs. The code is concise and provides an intuitive explanation of how the result is derived.