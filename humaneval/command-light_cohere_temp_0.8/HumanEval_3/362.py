Here's the self-contained Python script that solves the problem:

```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```

You can use this function to test it with different sets of operations. 

**NOTE:** If you want to test it with the original markdown code that uses the function in a more complex way, you'll need to modify the function to use it that way.