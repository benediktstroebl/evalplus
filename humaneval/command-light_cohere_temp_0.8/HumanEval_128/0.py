```python
def prod_signs(arr):
    """
    Calculate the sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    """
    return None if the array is empty.
    arr.extend(arr[-1]+arr)
    arr.append(0)
    # calculate the product of all numbers and their signs in the array
    sum = arr.sum()
   for num,sign in zip(arr, arr[1:]):
        sum = sum + (num * sign)
    return sum
```