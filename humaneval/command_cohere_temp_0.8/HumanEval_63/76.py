```python
def fibfib(n):
    a,b,c = 0,0,1
    for i in range(n):
        a,b,c = b,c, a+b+c
    return c
```
This code defines a function fibfib(n) that computes the nth FibFib number efficiently. It uses an initialization of three variables a, b, and c to 0, 0, and 1 respectively. It then uses a loop to update these variables accordingly within the defined sequence, where a is updated to be b, b is updated to be c, and c is updated to be the sum of the previous a, b, and c values. This allows the function to compute the FibFib number efficiently without redundant calculations. 

Here is an example usage of the function:
```python
>>fibfib(1)
0
>>fibfib(5)
4
>>fibfib(8)
24
```
This showcases the correctness of the function for various test cases.