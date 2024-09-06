```python
def can_arrange(arr):
    prev = arr[0]
    mx = arr[0]
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur < prev:
            mx = idx
        prev = cur
    return mx if mx != -1 else -1
```

The function traverses the array, maintaining two variables: `prev` to hold the value of the previous element, and `mx` to store the index of the current largest element not greater than the previous element. The function returns -1 if no such element is found. If an element is smaller than the previous one, the function updates `mx` and resets it to -1 if no suitable element is found towards the end. The function is concise and efficient, directly solving the problem statement. It provides a logical and scalable approach that achieves a time complexity of O(n), where 'n' is the length of the input array.