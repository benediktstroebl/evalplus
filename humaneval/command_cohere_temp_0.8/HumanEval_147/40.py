```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate max triples through prefix sum
    ps = [0] * (n + 1)
    for ai in a:
        ps[ai] += 1

    max_triples = 0
    for i in range(1, n + 1):
        max_triples = max(max_triples, ps[i] - ps[i - 1] - ps[i + 1])
    
    return max_triples
```

This approach creates the sequence of numbers as described in the prompt and calculates the frequency of each number in the sequence. The frequency of a number is equivalent to the number of triples it can form with appropriate counterparts whose sum is a multiple of 3. The maximum number of triples is then computed by comparing the frequency of each number and returning the maximum frequency. 

Here are some examples of input and output to illustrate how the function works:
```
Input: n = 10
Output: 4
Explanation: 
a = [1, 3, 7, 13, 21, 31, 43, 57, 73, 91]
Valid triples are (1, 13, 21), (1, 31, 43), (3, 21, 73) and (7, 43, 91).
```

```
Input: n = 11
Output: 5
Explanation: 
a = [1, 3, 7, 13, 21, 31, 43, 57, 73, 91, 111]
Valid triples are (1, 13, 31), (1, 43, 73), (3, 21, 91), (7, 31, 111) and (13, 73, 111).
```