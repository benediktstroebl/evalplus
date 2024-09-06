```python
def fibfib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b, a+b
    return a
```
This script defines a function 'fibfib' that takes a single argument 'n', representing the index of the desired FibFib number, and returns the n-th element of the FibFib sequence. It initializes two variables 'a' and 'b' with the first two elements of the sequence (0 and 1). It follows the definition of the FibFib sequence, where each number is the sum of the previous two elements. Using a loop that runs 'n-1' times, it updates 'a' and 'b' accordingly on each iteration, effectively calculating the desired FibFib number. The script efficiently computes the FibFib number in 'O(n)' time complexity, where 'n' is the input index, making it suitable for handling larger values of 'n'.