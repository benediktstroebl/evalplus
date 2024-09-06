```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem. It initializes a list `factorial_list` with values of factorials from 1! to n!. Then, it calculates the factorial of n by multiplying the last element in the list (`factorial_list[n]`) with `(n-1)!` and iterates this process until it reaches 1!. This is effectively the same approach as defined in the problem statement. 
The unit tests would usually be accompanied by the expected output for each test case, ensuring that the function produces correct results. This script is a simple yet self-contained solution to the problem statement, and it can be executed independently to validate its behavior.  Any special syntax or unidiomatic aspects have been avoided to ensure it adheres to Python coding best practices.  If you would like a different approach or have any other specific requirements, feel free to elaborate, and I'll be happy to adapt my response accordingly.