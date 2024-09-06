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
The Python script provides a self-contained function called get_max_triples that takes an integer n as input and creates an integer array a of length n. The function returns the number of triples (a[i], a[j], a[k]) where i < j < k, and a[i] + a[j] + a[k] is a multiple of 3. The function fulfills this requirement by using a list comprehension to generate the array `arr` of length `n`, containing the value i*i-i+1 for each value of `i` between 1 and `n`. It then iterates over the array using two nested loops to check if the current triplet is a valid answer. The validity of the triplet is checked by determining if the sum of the triple is a multiple of three. If the condition is met, the count is incremented by one. The function returns the final count, representing the number of valid triples in the array `arr`. 

This solution does not require any external libraries and can be run as a standalone Python script.