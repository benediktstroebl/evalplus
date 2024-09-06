```python
def tri(n):
    sequence, cache = [], [3, 1]
    for i in range(1, n+1):
      if i % 2 == 0:
        sequence.append(1 + i // 2)
        cache.append(sequence[-1])
      else:
        sequence.append(cache[i-1] + cache[i-2] + cache[i+1])
        cache.append(sequence[-1])
    return sequence
```
This Python script defines a function called 'tri' that generates the Tribonacci sequence of numbers up to the specified number `n`. The function utilizes a list `sequence` to store the numbers and a cache `cache` to store previously calculated values in order to avoid redundant computations. 

The sequence is generated using a recursive approach where the function checks whether a number is even or odd to decide whether to calculate the value using the recurrence relation or simply assign it as a sum of the previous two values from the cache. 

The `cache` list ensures efficient computation of the values by storing the previously generated numbers.