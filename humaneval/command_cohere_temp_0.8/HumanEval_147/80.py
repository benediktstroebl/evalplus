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
The Python script provides a function called `get_max_triples` accepting an integer `n` as an argument and aims to generate an array of length `n` where each element is computed as `i * i - i + 1` (where `i` varies from 1 to `n`). The function then counts and returns the number of triples in this array where the corresponding elements satisfy the condition that their sum is divisible by 3. This problem can be solved using two nested loops, the outer loop (`i`) picks elements from the array, and the inner loop (`j`) picks elements that are greater than the picked element `i`. Then the condition for being a multiple of three is checked for the sum of the elements `arr[i] + arr[j] + arr[j+1]`. The final count is returned as the answer.