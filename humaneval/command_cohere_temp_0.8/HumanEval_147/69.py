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
This Python script defines a function called 'get_max_triples' which takes an integer 'n' as input. This function calculates the maximum number of valid triples from the given 'n' elements in the array 'a' with the property that a[i] + a[j] + a[k] is a multiple of 3. It does so in the following manner:
- Firstly, it creates an array 'arr' that contains the intermediate results for the elements in the question. This is done using a list comprehension which calculates `i * i - i + 1` for each value of `i` between 1 and `n`.
- After the creation of the array, it begins a nested loop where the first loop iterates over each element `arr[i]` in the array. 
- The second loop iterates over each element `arr[j]` in the array where `i < j`. Both these loops are range(`n-2`) - 2 iterations less than the length of the array to avoid iterating over the edges.
- Inside the nested loops, there is a condition checking if the sum of the current `arr[i]`, `arr[j]`, and `arr[j+1]` is a multiple of 3. If this condition is true, the 'cnt' counter is incremented.
- Finally, the function returns the value of 'cnt', which is the number of valid triples found in the described scenario. 

This is one of the many approaches to solve this problem and behaves correctly as specified in the example provided.