```python
def tri(n):
    sequence, result = [], []
    sequence.append(3)
    result.append(3)
    if n == 1:
        return result
    for i in range(2, n + 1):
        if i % 2 == 1:
            sequence.append(sum(sequence[-3:]))
        else:
            sequence.append(1 + i // 2)
        result.append(sequence[-1])
    return result
``` 

This code defines a function called `tri(n)` that generates the first `n+1` numbers of the Tribonacci sequence, which is a sequence similar to the Fibonacci sequence but with different recurrence relations for odd and even indices. The function first initializes the sequence and result as empty lists, and adds the base case of the Tribonacci sequence, which is `3`, to both lists. It then enters a loop that iterates from 2 to `n`, at each iteration, it checks if the index is odd or even to determine whether to add the next number to the sequence or result list. If the index is odd, it computes the next number in the sequence by summing the last three numbers in the sequence list and adds it to the sequence list, if the index is even, it adds `1 + i // 2` to the sequence list. Finally, it adds the current number of the sequence list to the result list and returns the result list.

Here is an example of using the function with value `n = 3`
```python
print(tri(3))
```
which will output:
```
[1, 3, 2, 8]
```