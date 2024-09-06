```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function `add()` takes a list of integers `lst` as an argument and aims to return a list of all even numbers present at odd indices of the original list. The function starts by creating an empty list called `even_odd` to store the odd-indexed even numbers. Then, it iterates through the input list using a `for` loop with the loop variable `i`. It monitors two factors:
1. `i` is incrementally checked for being an odd index in the list `lst` — this is determined by the expression `i % 2 == 1`.
2. The element at the current odd index `lst[i]` is checked to be an even number — this is determined by the expression `lst[i] % 2 == 0`.

If both conditions are true for a particular element at an odd index, that even number is added to the `even_odd` list. Finally, the function returns this list. 

The function is self-contained and does not require any external variables or modules, making it easy to use and integrate into other projects. It also follows the problem description and the provided example in the given markdown code block. 

This function can be improved by implementing optimizations, such as checking if each element in the list is even or odd only once, rather than twice. However, the current implementation is straightforward and effective for the described problem.