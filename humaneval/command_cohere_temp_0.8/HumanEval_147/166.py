```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum number of triples where a[i] + a[j] + a[k] is a multiple of 3.
    # We count the number of triples where the sum is 0, 3, 6, 9, ... , 
    # By factoring out 3, we can simplify this to 0, 1, 2, 3, ... , n-1.
    max_triples = sum(1 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n) 
                      if (arr[i] + arr[j] + arr[k]) % 3 == 0)
    
    return max_triples
```

This approach calculates the desired quantity directly, counting the number of triples where the sum of values is 0, 3, 6, 9, ... , n-1, and then factoring out 3 to simplify the problem. This solution is linear in the number of triples, which is O(n^3). 

The total time complexity is O(n^3) and the total space complexity is O(1). 

This solution is efficient and follows the seasonal coding norms. It is valuable to ensure that the code behaves correctly with respect to edge cases, handling smaller inputs first and then progressively larger inputs. This helps in ensuring that the code is correct for all cases and reduces the chance of any hidden bugs.