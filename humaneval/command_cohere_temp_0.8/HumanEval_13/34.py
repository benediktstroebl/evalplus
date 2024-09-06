```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This straightforward solution uses recursion by maintaining the invariant that `b` cannot be 0, until it is, at which point the base case is reached and the function returns `a`. 

A more efficient solution would be to calculate the GCD using the Euclidean Algorithm, which is a variation of the approach above. The solution minimizes the number of operations required to calculate the GCD and has a time complexity of `O(log(min(a,b)))`. Below is an example implementation of this method: 
```python
def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a
```
This can be tested in the same way as the original function, checking that it returns the correct GCD for a range of inputs.