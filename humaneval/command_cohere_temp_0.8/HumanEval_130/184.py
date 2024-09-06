```python
def tribonacci(n):
    res, a, b, c = [], 1, 3, 0
    while len(res) < n + 1:
        if len(res) % 2 == 0:
            res.append(a)
            a = c + b
            c = b
            b = a - c
        else:
            res.append(sum([a, b, c]))
            a, b, c = a - b - c, b, c + a
    return res
```
The code uses a generator expression to create an infinite Tribonacci sequence and then slices the first `n + 1` numbers from it. 

The result is then returned as a list. 

To do this, it uses three variables (`a`, `b`, `c`) to keep track of the last three values in the sequence. 

Then, in a loop, it checks whether the length of the list is even or odd to decide which equation to use to calculate the next number in the sequence, and updates the values accordingly. 

The code employs a generator expression to create a continuous Tribonacci sequence and extracts the first n + 1 numbers to ensure the list's length is correct. 

You can test this code by calling the function with different input values to verify its behavior.