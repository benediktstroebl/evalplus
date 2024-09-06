```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    triples = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if (arr[i] + arr[j] + arr[j+1]) % 3 == 0:
                triples += 1
    return triples
```
The script defines a function `get_max_triples` which takes an integer `n` as input and creates an array `arr` of length `n` based on the problem's given formula. It then calculates the number of triples where the sum of the three array elements is divisible by 3 and stores it in the variable `triples`. The function returns the calculated number of triples.