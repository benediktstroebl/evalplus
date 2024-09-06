Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    ans = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ans.append(factorial(i))
        else:
            ans.append(sum(range(1, i+1)))
    return ans

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
```
This script defines two functions:
- The `f` function takes an integer `n` as input and returns a list where the i-th element is the desired value, either the factorial of i or the sum of numbers from 1 to i, depending on whether i is even or odd, respectively. 
- The `factorial` function calculates the factorial of a given number `n` by multiplying `n` with all numbers from 1 to `n`. 

The `f` function uses a `for` loop to iterate through numbers from 1 to `n`, and for each number, it checks if it's even or odd to decide whether to append the factorial of `i` or the sum of numbers from 1 to `i` to the growing list. The `factorial` function, in turn, uses a for loop to iterate through numbers from 1 to `n` and multiplies them together to calculate the factorial. 

This solution complies with the given problem statement and example, and the code is self-contained and efficiently solves the problem. 
**NOTE**: Using `range` instead of a list comprehension for the `factorial` function is more efficient as the domain reduces by 1 at every step, avoiding unnecessary work.