```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] + arr[j-i-1]) % 3 == 0:
                triples += 1
    return triples
```
The solution is based on the observation that each triplet (a[i], a[j], a[k]) forms a triangle where the sum of the triangle’s three sides are divisible by 3. If we count all the triangles with sides less than or equal to n, whose triangle’s sides’ sum is divisible by 3, then we will get the answer to the problem. Since the maximum value a side of the triangle can take is n, therefore the number of triangles with sides less than or equal to n is less than or equal to n*(n+1)/2. The number of triangles that have their sum divisible by 3 is 1/2*n*(n+1)/2. The rest is easily achievable via simple scripting.