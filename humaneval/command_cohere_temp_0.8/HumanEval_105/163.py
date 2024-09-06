```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', 
                  '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
    result = [transf_map[int(i)] for i in sorted_arr if int(i) in range(1, 10)]
    return result if result else []
```

The aforementioned function initiates by sorting the provided array in descending order using the sorted function coupled with the reversed parameter.[^1] Subsequently, the function transforms each digit into its respective name from "One" to "Nine" and stores these transformed values in the `transf_map` dictionary. The digit-to-name conversion is accomplished by iterating over the sorted array and applying the `int` function to each element; thereby, qualifying it for inclusion in the range from 1 to 9. The resultant transformed array is then returned; however, an empty array is returned if the input array is void. 

[^1]: The parameter `reverse` in the `sorted` function, when set to `True`, arranges the elements in a descending order.