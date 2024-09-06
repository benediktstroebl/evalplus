```python
def tri(n):
    sequence, cache = [], [3, 1]
    for i in range(1, n+1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(cache[i-1] + cache[i-2] + cache[i+1])
        cache.append(sequence[-1])
    return sequence
```
This Python script defines a function called 'tri' that generates the Tribonacci sequence of numbers for a given input 'n'. The function utilizes a list called 'sequence' to store the numbers of the sequence and another list named 'cache' to keep track of already calculated values needed for the progression of the sequence. For each number 'i' from 1 to 'n', the function checks if the number is even or odd to decide whether to add the number to the sequence or calculate the sum of the previous and following numbers in the sequence. Finally, the 'sequence' list is returned, containing the first 'n' plus 1 numbers of the Tribonacci sequence.