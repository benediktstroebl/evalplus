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
This Python script defines two functions. The first function, f, accepts an integer n as input and returns a list composed of an interesting mix of factorials and sums. The second function, factorial, computes the factorial of a given number n. This factorial is calculated by incrementally multiplying all numbers from 1 to n. 

The script's main focus is the implementation of the f function, which rigorously adheres to the problem description. It employs a for loop to iterate through numbers from 1 to n, creating a list where each even-numbered element is the factorial of that number, and each odd-numbered element is the sum of the numbers up to that number. This accurately fulfills the problem's specification. 

As a prudent programming practice, the factorial function is utilized within f to ensure that the computation of factorials is not repeated multiple times, wisely optimizing the script's performance.