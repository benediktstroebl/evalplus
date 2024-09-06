```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] + arr[j + 1]) % 3 == 0:
                cnt += 1
    return cnt
```
This script creates the array of values and counts valid triples using two nested loops. The outer loop increments a counter for each valid triple, as determined by the condition that the sum of the values in the triple is a multiple of 3. This condition is assessed using the modulus operator (`%`). The function then returns the counted number of valid triples. This code efficiently solves the problem without introducing unnecessary complexities.