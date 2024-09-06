```python
def specialFilter(nums):
    odd_digits = [x for x in nums if int(x) > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(odd_digits)
```

This function `specialFilter` takes an array of numbers (`nums`) as input and returns the number of elements in the array that meet the following criteria:
1. Intgreater than 10` implies that the focus is on elements that are greater than 10.
2. `int(str(x)[0]) % 2 == 1` ensures that the first digit of the number is odd (`1`, `3`, `5`, `7`, or `9`).
3. `int(str(x)[-1]) % 2 == 1` ensures that the last digit of the number is odd.

The function filters the array accordingly and returns the count of such elements. 

This solution ranks among the top solutions in terms of efficiency since it uses a single list comprehension for filtering without requiring any additional loops. Thus, its time complexity is O(n), where `n` is the length of the input array.