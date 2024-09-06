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
This script defines two functions:
1. The `f` function takes an integer `n` as input and returns a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from 1 to `i` otherwise. This is done using a for loop that iterates through numbers from 1 to `n`, and for each number, it checks if it's even or odd to decide which value to assign to the list.
2. The `factorial` function calculates the factorial of a given number `n` by iterating through all numbers from 1 to `n` and multiplying them by the `result` variable, which should be assigned to 1 for the first iteration and is multiplied by the current number for each new iteration. 

Such a nested iteration strategy allows the `f` function to generate the desired list of numbers as per the given problem.