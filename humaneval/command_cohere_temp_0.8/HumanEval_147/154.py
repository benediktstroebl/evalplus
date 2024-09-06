```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (arr[i] + arr[j] + arr[j+1]) % 3 == 0:
                triples += 1
    return triples
```
The Python script provides a self-contained function called get_max_triples that takes an integer n as input and creates an array a of length n where each element in the array is defined as i * i - i + 1 for all values of i from 1 to n. The problem asks to return the number of triples (a[i], a[j], a[k]) where i < j < k and the sum of any two elements in the triplet is divisible by 3. The script then uses two nested loops to check every pair of elements in the array and counts how many pairs have a third element that can complete the requirement, finally returning the number of qualifying triples.