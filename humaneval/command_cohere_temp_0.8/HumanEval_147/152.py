```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (a[i] + a[j] + a[j + 1]) % 3 == 0:
                triples += 1
    return triples
```

The function creates the sequence of numbers as described in the prompt and then iterates through all possible pairs of values excluding the last value. It then checks if the sum of the two values plus the next value in the sequence is divisible by three. This can be accomplished through the use of a for loop and checking if the modulus of 3 is equal to zero. To account for all possible triples, the outer loop iterates from the first value to the second to last value of the sequence. The inner loop does the same but stops before the last value. The reason for this is that you cannot have a triple that includes the last value of the sequence without the sum of the three values being divisible by three, so it is not necessary to check these combinations. The function then returns the number of qualifying triples.

This solution has a time complexity of O(n^2) due to the nested for loops and a space complexity of O(1) as it only uses a constant amount of extra space to store the sequence.