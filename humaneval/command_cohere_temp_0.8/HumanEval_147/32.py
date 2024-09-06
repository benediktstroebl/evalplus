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
This Python script defines a function called 'get_max_triples' which takes an integer 'n' as input. This function computes the maximum number of triples formed from an array of length 'n' where each element of the array is computed as i*i-i+1 for i ranging from 1 to n. The computed array is stored in the variable 'arr'. The function then iterates through the array 'arr' and counts the number of triples (a[i], a[j], a[k]) where 'i', 'j', and 'k' are indices such that 'i' < 'j' < 'k' and the sum of 'a[i]', 'a[j]', and 'a[k]' is divisible by 3. The count is stored in the variable 'cnt'. Finally, the function returns the value of 'cnt', which is the maximum number of eligible triples in the array 'arr'.