```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array if odd else reversed(array)) if array else array
```

The function sorts the array as explained in the prompt and works also for empty arrays. 

This solution favors simplicity and readability over pure performance, there's room for improvement in terms of time complexity, especially for large arrays.

I hope this solution aids you and feel free to ask if you would like further insights or have other questions!