```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if (arr[i] + arr[j] + arr[j+1]) % 3 == 0:
                cnt += 1
    return cnt
```
This Python script defines a function called 'get_max_triples' which takes an integer 'n' as input. This function computes the maximum number of triples with the property that the sum of the three values is divisible by 3. To achieve this, it generates an array 'arr' of length 'n' where each element is computed as 'i * i - i + 1' (where 'i' is the index). It then iterates through the array and counts the number of triples that satisfy the condition. This approach ensures that the code is self-contained and efficient in solving the given problem.