```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    triples = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if (arr[i] + arr[j] + arr[j+1]) % 3 == 0:
                triples += 1
    return triples
```
The script defines a Python function `get_max_triples` that takes an integer `n` as input and returns the number of triples from the given array `arr` where the sum is a multiple of 3. The function creates the array `arr` as stated in the problem and then uses two nested loops to iterate over all pairs of elements except the last one. It checks if the sum of the three elements is a multiple of 3 and updates the count accordingly. Finally, it returns the computed count of qualifying triples. 

You can use this code to solve the problem described in the markdown code block. Just execute the script and call the function with the appropriate input to get the desired output. For example:
```python
print(get_max_triples(5))  # Output: 1
``` 
This will produce the result of 1 for the given example in theMarkdown code block.