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
This Python script defines a function called `get_max_triples` that takes in a positive integer n as its input. Inside the function, it first creates an integer array a of length n, where each element a[i] is computed as i * i - i + 1 for all values of i from 1 to n. Then, it initializes a variable cnt to track the number of triples it finds. It iterates through the array with two nested loops, where the outer loop iterates from i = 1 to n - 2, and the inner loop iterates from j = i + 1 to n. This ensures it considers all valid pairs of elements a[i] and a[j] in the array. 

The condition (arr[i] + arr[j] + arr[j + 1]) % 3 == 0 checks if the sum of the three elements a[i], a[j], and a[j + 1] is divisible by 3, which indicates a valid triple. If this condition is met, the cnt variable is incremented, effectively counting the number of valid triples. Finally, the function returns the computed cnt value, representing the maximum number of triples that satisfy the given criteria in the array a.