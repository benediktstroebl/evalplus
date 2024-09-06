```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', 
                  '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
    result = [transf_map[dig] for dig in sorted_arr if dig in range(1, 10)]
    return result if result else []
```

The provided Python code defines a function `by_length` that performs the tasks specified in the problem statement. It first sorts the given array of integers between 1 and 9, reverses the sorted array, and then replaces each digit with its corresponding name from "One" to "Nine". The result is returned as a list. If the input array is empty, it returns an empty list, and if there are any unusual numbers in the array, they are ignored in the final result. 

The code is enclosed in a code block that allows you to easily run it and see the results. You can execute it in your preferred Python environment to observe the transformed output.