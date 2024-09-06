```python
def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
        signs_product = functools.reduce(lambda x, y: x * y, signs, 1)
        magnitudes = [abs(i) for i in arr]
        magnitudes_sum = sum(magnitudes)
        result = magnitudes_sum * signs_product
    return result
```

The algorithm to solve the given problem comprises of four primary steps:
1. Verify if the array is empty. If true, return `None` right away. 
2. Calculate the length of the array to utilize it for reducing calculations. 
3. Compute product of all signs using the `reduce` function, product of same signs yields the sign, while product of different signs yields `0`.
4. Calculate the sum of magnitudes of all numbers and multiply it by the product of signs. 

This combined operation provides the desired result. 

The comprehensive test cases are typically included to certify the performance of the function for varied inputs. These test cases encompass examples of both empty and non-empty arrays, and arrays with only positive, only negative, or both positive and negative numbers.