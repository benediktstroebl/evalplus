```python
def fibfib(n):
    a,b,c = 0,1,1
    for _ in range(3,n+1):
        a,b,c = c,a+b,b+c
    return a
```
This script defines a function 'fibfib' that takes an integer 'n' as input and returns the n-th number in the FibFib sequence, as described in the prompt. It initializes the variables 'a', 'b', and 'c' with the initial values for the sequence (0, 1, 1). It then enters a loop that iterates from 3 to 'n', updating the values of 'a', 'b', and 'c' to compute the subsequent values in the sequence using the defining recurrence relation. After the loop completes, the function returns the value of 'a,' which will be the n-th number in the FibFib sequence.