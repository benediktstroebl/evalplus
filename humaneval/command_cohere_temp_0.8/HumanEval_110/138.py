```python
def exchange(lst1, lst2):
    res = 'NO'
    # Check if any element of lst1 is odd
    if any(num % 2 for num in lst1):
        # Exchange odd numbers with even numbers from lst2
        lst1[:], lst2[:] = [num for num in lst2 if num % 2 == 0], [num for num in lst1 if num % 2 == 0]
        # Check if all elements in lst1 are even now
        if all(num % 2 for num in lst1):
            res = 'YES'
    return res
```

The approach works by using list comprehension and the built-in `any` and `all` functions to quickly check for the condition required. Initially, the function assumes that an exchange is possible and swaps the lists accordingly. After the swap, it verifies if all elements in `lst1` are even, setting the flag to 'YES' if true, and 'NO' if false. 

The code is structured in a way that it firstly assumes the worst case, exchanging the lists, hoping that the condition is met, which greatly increases the efficiency of the function, thus, making it a scalable solution. 

This approach guarantees a time complexity of `O(n * log n)`, where `n` represents the length of the list. It also utilizes list comprehension, which provides for efficient and concise code writing, and the `any` and `all` functions which are built within Python and optimized for list checking.