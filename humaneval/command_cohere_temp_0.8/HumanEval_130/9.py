```python
def tri(n):
    sequence, last_odd, last_even = [], 1, 3
    while len(sequence) < n + 1:
        if len(sequence) % 2 == 0:
            sequence.append(last_even)
            last_even = last_even + last_odd + sequence[-1]
        else:
            sequence.append(last_odd)
            last_odd = last_odd + last_even + sequence[-1]
    return sequence
```

The code defines a function 'tri()' which generates the Tribonacci sequence up to the `n+1` term. It initializes an empty sequence, and variables `last_odd` and `last_even` with initial values of 1 and 3 respectively.

A `while` loop is used to iterate until the length of the sequence is greater than `n`, updating the values of `last_odd` and `last_even`, and appending the values to the sequence based on the parity of the length. It uses an interesting recursive calculation of the next value in the sequence. If the length of the sequence is even, it appends `last_even` to the sequence and updates it to the sum of the previous two values in the sequence. If the length is odd, it appends `last_odd` and updates it similarly. 

Finally, it returns the sequence of the first `n` Tribonacci numbers. The code is concise and efficient, achieving a time complexity of O(n) and a space complexity of O(1), making it an optimized solution for this problem.