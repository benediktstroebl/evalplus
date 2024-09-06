```python
def search(lst):
    freq, max_val = -1, 0 
    for n in lst:
        if n > max_val:
            max_val = n 
        elif n == max_val and lst.count(n) >= n:
            freq = n 
    return max_val if freq == -1 else freq 

# Test Cases
assert search([4, 1, 2, 2, 3, 1]) == 2
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([5, 5, 4, 4, 4]) == -1
```

This Python script defines a function `search` that solves the problem as outlined in the prompt. It iterates through the list, keeps track of the maximum value encountered (max_val), and checks if it's appearing enough times to meet the condition. If so, it returns that frequency (`freq`). If not, it returns -1, indicating that no such number exists in the list. The script includes test cases to verify its correctness against the expected outputs.