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
This Python script defines two functions. The first function, `f`, takes an input `n` and returns a list where each element's value depends on its index's parity. If the index is even, the element's value is the factorial of that index, calculated using a recursive function. If the index is odd, the element's value is the sum of numbers from 1 to that index. This function encapsulates the core logic of the problem. 

The second function, `factorial`, is a helper function used by `f` to calculate the factorial of a given number `n` using a recursive approach. It multiplies the `num` variable by each number from 1 to `n` in a loop. 

Overall, the script provides an accurate and efficient solution to produce the required list of values, making it a comprehensive implementation for the problem.