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
This script creates the array of values and counts valid triples using two nested loops. The outer loop selects the first element of the triple, and the inner loop selects the second and third elements. If the sum of the three array items is divisible by three, the function counts it as a valid triple. The final count of valid triples is returned. 

The example provided in the original problem description would return 1 as the answer, as the valid triple in the array is (1, 7, 13).