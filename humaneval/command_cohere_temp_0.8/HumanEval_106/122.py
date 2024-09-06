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
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
This Python script defines two functions. The first function, `f`, takes an input `n` and returns a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from 1 to `i` otherwise. The second function, `factorial`, calculates the factorial of a given number `n` by multiplying `n` with all numbers from 1 to `n`. 

The example provided in the prompt would generate the following outcome:
```python
f(5) == [1, 2, 6, 24, 15]
```

This code provides an example of how to solve problems that involve mathematical concepts like factorial in a programming context. 
If there are further questions or any other tasks that you'd like to accomplish with coding, feel free to ask!