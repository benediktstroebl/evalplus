```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            if curr % 3 == 0:
                triples += 1
            elif curr % 3 == 1:
                # Subtract occurrences of curr as both pairs (a[i], a[j]) and (a[j], a[k]) are counted
                triples -= occurrences_of(curr, a)
            elif curr % 3 == 2:
                # Add occurrences of curr as both pairs (a[i], a[j]) and (a[j], a[k]) are counted
                triples += occurrences_of(curr, a)
    
    return triples

def occurrences_of(number, lst):
    # Count the occurrences of a number in a list
    return sum(1 for i in lst if i == number)
```

The solution calculates the sum of triples meeting the requirement in the problem statement. The key insight is that when `a[i] + a[j] + a[k]` is a multiple of 3, at least two of the three values must contribute a factor of 3. Therefore, we use a combination of addition and subtraction based on the remainder of `a[i] + a[j]` as we iterate through the array.

The self-contained function `occurrences_of` counts the number of occurrences of a particular number within a list. This is achieved using a sum and a generator expression.