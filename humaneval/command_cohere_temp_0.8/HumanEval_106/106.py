```python
def f(n):
    li = [0] * n
    for i in range(1, n+1):
        if i % 2 == 0:
            li[i-1] = factorial(i)
        else:
            li[i-1] = sum(range(1, i+1))
    return li

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The `f` function uses a list comprehension to create a list with `n` elements where the i-th element is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise. To do this, it uses a `for` loop that iterates through each element in the list from the second to the last element included. It checks if the current index is even through the `% 2 == 0` expression, and if so, it calculates the factorial of i using the `factorial` function and assigns it to the i-th element of the list. If the index is odd, it calculates the sum of numbers from 1 to i and assigns it to the i-th element of the list. 

The `factorial` function is a helper function used to avoid recursion and compute the factorial of a given integer `n`. It uses a `for` loop to iterate through each number from 1 to `n` and multiplies the `result` variable by the current number to approximate the factorial.

The provided code solves the problem and passes the tests as it returns a list of size n where the value of the element at index i is the factorial of i if i is even or the sum of numbers from 1 to i otherwise. For example, f(5) will return [1, 2, 6, 24, 15].