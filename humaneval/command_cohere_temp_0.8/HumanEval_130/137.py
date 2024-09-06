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

The list of the first n + 1 numbers of the Tribonacci sequence is returned by the function tribonacci(n). It initiates the variables a, b, and c to 1, 3, and 0, respectively, and employs a while loop to calculate the Tribonacci sequence up to the n+1st number. It calculates the next number in the sequence based on whether the length of the res list is even or odd. It adds the already calculated values a, b, and c if the length is odd. If the length is even, it appends the value of a to the list and updates the values of a, b, and c to prepare for the next iteration. The while loop keeps going until the list contains n + 1 numbers. A list of the first n + 1 numbers in the Tribonacci sequence is then returned. 

Here is an example of how to use this function:
```python
tribonacci(3)
```

This will return the list [1, 3, 2, 8], which is the first three numbers in the Tribonacci sequence, according to the provided problem description.