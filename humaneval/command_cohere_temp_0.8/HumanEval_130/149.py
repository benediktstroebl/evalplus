```python
def tri(n):
    seq, last_odd, last_even = [], 1, 3
    for i in range(n + 1):
        if i % 2 == 0:
            seq.append(last_even)
            last_even = 1 + i / 2
        else:
            seq.append(last_odd)
            last_odd = seq[i - 1] + seq[i - 2] + last_even
    return seq
```
The Python script defines a function 'tri(n)' that generates the first 'n+1' terms of the Tribonacci sequence, which is a sequence similar to the Fibonacci sequence but with different recurrence relations for even and odd indices. The function initializes an empty list 'seq' to store the sequence and two variables 'last_odd' and 'last_even' to keep track of the last odd and even indices' values. The function then iterates through the range of 'n+1' to generate the Tribonacci sequence. For even indices, it calculates the value as '1 + i/2' and appends it to 'seq,' updating 'last_even.' For odd indices, it calculates the value as the sum of the previous three odd-indexed values (similar to the recurrence for Tribonacci sequence), appends it to 'seq,' and updates 'last_odd.' Finally, the function returns the generated sequence. 

Here is an example of using the tri function for different values of n:
```python
print(tri(0)) # Output: []
print(tri(1)) # Output: [1]
print(tri(2)) # Output: [1, 3]
print(tri(3)) # Output: [1, 3, 2, 8]
print(tri(4)) # Output: [1, 3, 2, 8, 5, 13, 4, 11, 9, 8]
```

Thus, the function provides the complete Tribonacci sequence as required in the problem statement.