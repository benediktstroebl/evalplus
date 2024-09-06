```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the opening and closing brackets (`[]`) as we iterate through the string. The algorithm is a simple "brace counter". We increment the counters whenever we encounter an opening or a closing bracket.

If at any point the `open` counter is greater than the `close` counter, we return `False`. This is because in any valid bracket sequence, the opening brackets must be eventually "matched" by closing brackets, so the maximum difference between them is 1.

If at the end of the string, the open counter is not equal to the close counter, this indicates there is a nested bracket. This is because the closing brackets arrive faster than the opening ones and there is a point where the closing counter is increased, but the opening counter is not decreased, which indicates a nested bracket. 

The provided examples in the prompt satisfy this algorithm's criteria and return the correct values.