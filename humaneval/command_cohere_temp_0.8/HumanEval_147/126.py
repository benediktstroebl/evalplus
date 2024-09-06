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
The Python script provided solves the problem by creating a list of numbers from 1 to n in a way that each number is an integer cube distance away from the next number. It then counts the number of valid triples, that is, three numbers that are integer cube distances apart and whose sum is a multiple of 3. This problem exemplifies a case where Python's functional and iterative style can be combined with a clear problem understanding to provide a clean and efficient solution.