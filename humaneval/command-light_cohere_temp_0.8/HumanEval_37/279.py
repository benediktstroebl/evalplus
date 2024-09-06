```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1:] + [x for x in lst[0] if x % 2 == 0]]

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6]
    even_sorted = sort_even(test_list)
    print("Test list:", even_sorted)

    test_list = [5, 6, 3, 4]
    odd_sorted = [x for x in test_list if x % 2 == 0]
    print("\nTest list:", odd_sorted)

    test_list = [3, 6, 5, 4, 2]
    even_sorted = [x for x in test_list if x % 2 == 0]
    print("\nTest list:", even_sorted)

    test_list = [5, 6, 2, 3, 4]
    odd_sorted = [x for x in test_list if x % 2 != 0]
    print("\nTest list:", odd_sorted)
```

The code defines a function called sort_even that takes a list lst as input and returns a new list lst' that is a permutation of the list that maintains even values. The function achieves this in a loop, it takes the first element of the list, then creates a new list with the same elements from the original list, but with the exception of the first element. The loop will then loop, and will append the second element of the list, then the third, and so on, until it reaches the end of the list.