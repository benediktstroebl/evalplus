```python
def search(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return max(freq)

# Example usage:
lst = [4, 1, 2, 2, 3, 1]
print(search(lst))  # Output: 3
```