Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to increment each element in the input list by 1 and provide a result. It avoids unnecessary list copying and offers a more efficient solution.

Here is an example of how you can use the function to test it:
```python
test_list = [1, 2, 3]
result = incr_list(test_list)
print(result)
``` 

This should produce the following output:
[2, 3, 4]
This approach aligns with problem guidelines, incorporating the function incr_list into the test script for comprehensive evaluation.