```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` parameter of the `sort` method is used to specify a function that returns the parameters to be used for sorting. In this case, we define a lambda function that takes an element of the list and returns a tuple whose first element is `-bin(x).count('1')` and the second one is `x`, the element itself. The `-` before the result of the `bin` method is used to convert an integer to a binary string and the `count` method returns the number of occurrences of the passed argument in the string. Since we want to sort in ascending order, we are returning the result as negative. In this way, elements with more ones will appear first and if there is a tie, it will sort elements according to their decimal value.