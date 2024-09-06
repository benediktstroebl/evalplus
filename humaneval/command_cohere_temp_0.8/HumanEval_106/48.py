Here is a Python script that solves the problem you have described:
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
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```
The `f` function takes an integer `n` as input and returns a list where the i-th element is the factorial of i if i is even, or the sum of numbers from 1 to i otherwise. The factorial of a number is calculated using the `factorial` function. This is a recursive function that calculates the factorial of a number `n` by multiplying `n` with the factorial of `n-1` if `n` is greater than 1, and returns 1 if `n` is 1. 

The code above solves the problem and passes the test case mentioned in the description, as the output of `f(5)` is `[1, 2, 6, 24, 15]`.  This is because the elements at index 1, 3, and 5 are even, and the rest are odd. Thus, the elements calculated are:
- Element at index 1: 1 * 2 = 2
- Element at index 3: (3 * 4 * 5) = 60
- Element at index 5: (5 * 4 * 3 * 2 * 1) = 600

The remaining elements are calculated using the sum of numbers from 1 to i, which yields the remaining values:
- Element at index 2: sum(range(1, 3)) = 1 + 2 = 3
- Element at index 4: sum(range(1, 5)) = 1 + 2 + 3 + 4 = 10 
The rest of the elements in the list are calculated similarly.  Please note that the sums could be calculated in a more optimized manner, but for the sake of simplicity, they are computed using the `range` function.  This solution provided by the `f` function fulfills the condition mentioned in the prompt.