```python
def tri(n):
    ans = [1, 3]
    if n > 1:
        ans += [2] * (n - 2)
    for i in range(1, n):
        if i % 2 == 1:
            ans.append(ans[i - 1] + ans[i - 2] + ans[i + 1])
        else:
            ans.append(1 + i // 2)
    return ans
```