```python
def match_parens(lst):
    def check(s, arr):
        cnt = [0] * 2
        for ch in s:
            if ch == '(':
                cnt[0] += 1
            else:
                cnt[1] += 1
            if not arr[cnt[0]]:
                return False
            if not arr[cnt[1]]:
                return False
        return cnt[0] == cnt[1] == 0

    return "Yes" if any(map(check, lst)) else "No"
```

The following is a breakdown of the code:
1. An inner function `check(s, arr)` is defined to check the parentheses balance of any given string `s` using a counter for '(' and ')' and checking against the input array `arr`.
2. The main function invokes `check()` for various combinations of input strings using the `any()` function, ultimately returning "Yes" if any combination is viable and "No" otherwise.

This approach allows the code to cleanly and efficiently validate whether any permutation of the input list creates a balanced string.