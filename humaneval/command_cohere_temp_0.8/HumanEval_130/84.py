```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0] + tribonacci(n - 1)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```
The function takes an input of type integer, and returns a list of numbers of the Tribonacci sequence, by using simple if statements and returning a list of zeros for the even index of n in the Tribonacci sequence or returning list of 1 and adding the previous 2 lists of theTribonacci sequence (n - 1 and n + 1) for the odd index of n. 

Here is a simple test to validate the function:
```python
test = tribonacci(0)
print(test)
```
Expectation: [0]

 actuality: 
```
[0]
```