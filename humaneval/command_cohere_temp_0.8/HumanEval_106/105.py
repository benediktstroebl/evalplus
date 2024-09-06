Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    li = []
    for i in range(1, n+1):
        if i % 2 == 0:
            li.append(factorial(i))
        else:
            li.append(sum(range(1, i+1)))
    return li

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Tests:
print(f(5))
# [1, 2, 6, 24, 15]
```
This script defines a function `f` that takes an integer `n` as input and creates a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from 1 to `i` otherwise. The function uses a loop to calculate the factorial of a number, and the sum of numbers from 1 to `i` is calculated using the `range` function. The provided example output is also printed. 

The code above utilizes a loop to compute the factorial of a number `n`, which is a recursive function, and can be very computationally expensive for large inputs. It runs at `O(n)`, which is not very efficient; you might need to optimize it based on the input size.