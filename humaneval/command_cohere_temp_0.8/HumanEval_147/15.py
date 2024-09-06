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
This script creates the array of integers as described in the prompt and then counts the number of triples meeting the requirement. Such triples cause the sum of a[i], a[j], and a[k] to be divisible by 3. It uses two nested loops to iterate through all possible pairs of integers and calculates if their sum is divisible by three. The outer loop is responsible for the first element of the triple, and the inner loop is responsible for the second and third elements. Finally, it returns the count of valid triples.