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
The `f` function uses a list comprehension to create a list with `n` elements, where each element is initialized to 0. It then loops through the numbers from 1 to `n` and, using an if statement, determines whether each number is even or odd. If the number is even, it computes the factorial of that number and assigns it as the value of the corresponding list element. If the number is odd, it computes the sum of numbers from 1 to that number and assigns it as the value of the corresponding list element. The `factorial` function is also included to calculate the factorial of a given number `n` by iterating through the numbers from 1 to `n` and multiplying them together, effectively computing the product of all the numbers up to `n`.  The result is stored in the `result` variable and returned. 
The solution is optimized for efficiency, using simple loops to achieve the desired functionality without requiring complex algorithms or data structures. F performs the computations directly and assigns the result to the corresponding index in the list, ensuring the list is correctly populated in linear time.