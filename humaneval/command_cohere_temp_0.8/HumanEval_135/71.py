```python
def can_arrange(arr):
    prev = arr[0]
    ans = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur == prev:
            continue
        else:
            prev = cur
            ans = idx
    return ans
```

The function `can_arrange()` iterates over the entire array, comparing each element to the one preceding it. If an element is greater than its previous one, the function returns -1 immediately, indicating no suitable element. When an element is not greater than the previous one, we check if they are equal; in this case, we skip ahead as the answer is not viable. Otherwise, we update our answer index and check if the current element is suitable. The final index of this loop will be our final answer.