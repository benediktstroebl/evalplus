Here is a Python script that implements the function f in a way that is both efficient and easy to read:
```python
def f(n):
    return [
        factorial(i) if i % 2 == 0 else sum(range(1, i + 1)) for i in range(1, n + 1)
    ]

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
This script defines two functions: f takes an integer n as input and returns a list where each element is either the factorial of an even index or the sum of the integers from 1 to an odd index; the factorial function calculates the factorial of a given integer n. 

Both functions are written using only for loops, which is the simplest and most efficient approach for these particular tasks. The factorial function is natively efficient due to the inherent property of the product operation in Python, which performs very quickly when using small integers.

This code can efficiently handle lists of any size due to the linear time complexity of both the 'factorial' and 'sum' functions. Additionally, this code can handle large integers due to Python's integer multiplication implementing iterative algorithms, also with linear time complexity. Thus, even though the product operation is native, the space complexity remains O(1) as there are no additional spaces taken.

The list comprehension within the 'f' function would also operate in linear time, bringing the overall time complexity of this function to O(n). This simplicity and efficiency align with the style of Python, which prioritizes readability and computational efficiency respectively. 

These characteristics make the code very robust against larger inputs while remaining easy to understand.