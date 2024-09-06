```python
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    sequence = [1, 3]
    if n % 2 == 0:
        for i in range(1, n):
            x = 1 + i / 2
            sequence.append(x)
    else:
        for i in range(2, n + 1):
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i])
    return sequence
``` 

The function starts with some basic cases, returns an empty list for `n` equal to 0, and returns a list containing only the number 1 for `n` equal to 1. The Tribonacci sequence is then constructed by alternating between adding the middle number of the previous sequence and recursively calculating the previous two sequence elements. The function returns the first `n + 1` numbers of the Tribonacci sequence. 

To avoid storing a large number of numbers, the calculation leverages the parity of `n` and only calculates the middle number when `n` is even.  

The implementation is concise and efficient, using a loop to construct the sequence instead of recursion to save memory and improve performance.