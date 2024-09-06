```python
def sort_array(array):
    odd, even = array[:1], array[-1:]
    if sum(map(len, (odd, even))) % 2 == 0:
        array = sorted(array)[::-1]
    return array
```
This Python script solves the problem by dividing the array into two parts: `array[:1]` which corresponds to the first element (index = 1) and `array[-1:]` which corresponds to the last element (index = -1). Then, depending on whether the sum of the lengths of these two parts is even or odd, it reverses the entire array if the sum is even, and leaves it as it is if the sum is odd. This creates an effect where the array is sorted in descending order if the sum is even, and sorted in ascending order if the sum is odd, as per the problem statement.