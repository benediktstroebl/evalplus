```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (arr[i] + arr[j] + arr[j + 1]) % 3 == 0:
                triples += 1
    return triples
```

The script uses nested loops to iterate through the array `arr` that represents the values of the corresponding elements and checks if `arr[i] + arr[j] + arr[j + 1]` is a multiple of 3, which indicates the validity of the triplet. The script keeps track of the number of valid triplet occurrences using the `triples` variable and returns it upon function termination.

You can test this function against test cases and expect the maximum number of triples for n <= 10 to be the correct value. For instance, for n = 5, the result is 1, and the following code will print 1 as output:
```python
print(get_max_triples(5))
``` 
Please note that this code expects the input `n` to be of type `int` and greater than or equal to 1.