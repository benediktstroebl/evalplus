```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the output. 

This approach ensures that the function is optimized for efficiency and can handle various input scenarios while maintaining clarity and readability. Let me know if you'd like me to explain any of the steps in more detail or provide additional insights!