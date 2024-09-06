```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The `search` function employs a dictionary (`freq`) to tally the occurrence of each integer in the input list. Subsequently, it determines the maximum value of the frequency greater than or equal to the value of the integer itself. If no such integer is found, it returns -1. If multiple integers satisfy the condition, it returns the largest among them. 

Here is an example of how you can call the function for a given list:
```python
search([1, 2, 2, 3, 3, 3, 4, 4, 4])
```
Which yields the result of 3. 

This approach yields a time complexity of O(n) and a space complexity of O(n). It is a concise and efficient solution to the problem.