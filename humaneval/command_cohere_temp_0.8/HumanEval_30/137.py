```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension to filter out elements that are not positive numbers, offering a clean and concise solution. 

Such a solution adheres to Python's philosophy of emphasizing simplicity and readability, making it an ideal choice for coding challenges. 

The function can be tested like this:
```python
test_list = [-1, 2, -4, 5, 6]
assert get_positive(test_list) == [2, 5, 6]
``` 

And the expected output of 1:
```
[]
``` 

Is due to the fact that the list comprehension feature of Python 3.5 and later versions provides a concise and clear solution for filtering lists, making it a valuable tool for solving coding challenges.