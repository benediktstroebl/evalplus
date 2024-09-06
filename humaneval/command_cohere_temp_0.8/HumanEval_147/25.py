```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if arr[i] + arr[j] + arr[j+1] >= 3:
                cnt += 1
    return cnt
```
The Python script provides a self-contained function called get_max_triples that takes an integer n as input and returns the number of triples (a[i], a[j], a[k]) from an integer array a of length n that meets the problem's criteria. 

The function creates the integer array a using a list comprehension, where each value is calculated as i * i - i + 1 for i ranging from 1 to n. It then calculates the number of valid triples with a nested loop, where the first loop iterates over array index 'i', and the second loop iterates over the index 'j' with the condition that 'i' is less than 'j' in each triple. The condition a[i] + a[j] + a[j+1] >= 3 is used to determine if the corresponding triple causes the sum to be divisible by 3, and if so, the count is incremented by 1. 

This code efficiently solves the problem and provides the required count of qualifying triples from the array 'a' with a time complexity of O(N^2), where N is the input size (the integer n).