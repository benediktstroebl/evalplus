Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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

# Tests:
assert f(1) == [1]
assert f(2) == [1, 2]
assert f(5) == [1, 2, 6, 24, 15]
```
The code defines a function `f` that fulfills the requirements stated in the prompt, and the factorial function is correctly defined and used. The example usage and assert statements demonstrate the expected behavior of the function `f` and ensure that the code is correct and conforms to the provided problem statement. 
The time complexity of the given code is O(n) due to the loop in the `f` function, and the space complexity is O(n) due to the creation of the `li` list.