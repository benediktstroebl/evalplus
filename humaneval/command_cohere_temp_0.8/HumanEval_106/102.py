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
```
The `f` function uses a list comprehension to create a list where each index is initialized with a 0 value. Following the algorithm described in the problem, the function then loops through the list of indices from 1 to `n`, where `n` is the size of the output list. If the index is even, it sets the corresponding list element to the factorial of that index using the `factorial` function. If the index is odd, it calculates the sum of numbers from 1 to that index and assigns it to the corresponding list element.  The `factorial` function is a helper function used to calculate the factorial of a given number, which is needed for the even indices. 

This solution provides an algorithm to solve the given problem and a helper function to support the main algorithm. It is self-contained and can be executed independently.  It can produce the expected output for the example in the problem description: `f(5) == [1, 2, 6, 24, 15]`.  If you would like to test other input values, the `f` function is ready for direct use.  You can add additional test cases in the body of the script or through command line arguments when executing the script.  This will help ensure that the function remains correct for other inputs as well.